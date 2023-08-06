from uuid import uuid4
import time
import logging
import platform

from pulsar import new_event_loop
from pulsar.apps.data import create_store
from pulsar.apps.greenio import GreenHttp
from pulsar.apps.http import HttpClient

from ..utils.time import get_time
from ..tasks import models
from ..tasks import states
from ..tasks.task import Task, TaskNotAvailable
from ..backends import brokers
from ..mq import TaskManager

from .consumer import ExecutorMixin
from .pubsub import PubSub


class TaskProducer(models.RegistryMixin, ExecutorMixin):
    """Produce tasks by queuing them

    Abstract base class for both task schedulers and task consumers
    """
    app = None

    def __init__(self, cfg, *, logger=None, **kw):
        self.cfg = cfg
        self.logger = logger or logging.getLogger('pulsar.queue')
        self._closing = False
        loop = cfg.params.pop('loop', None)
        store = create_store(cfg.data_store, loop=loop)
        if not cfg.message_broker:
            broker = store
        else:
            broker = create_store(cfg.message_broker, loop=loop)
        self.manager = (self.cfg.callable or TaskManager)(self)
        self.pubsub = PubSub(self, store)
        self.broker = brokers.get(broker.name)(self, broker)
        self.http = self.manager.http()
        self.green_pool = self.manager.green_pool()

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return 'task producer <%s>' % self.broker

    @property
    def _loop(self):
        return self.broker._loop

    @property
    def node_name(self):
        return platform.node()

    async def start(self, worker=None):
        await self.pubsub.start()
        return self

    def queues(self):
        return ()

    def gen_unique_id(self):
        return uuid4().hex

    def lock(self, name, **kwargs):
        """aquire a distributed global lock for ``name``
        """
        return self.pubsub.lock('lock-%s' % name, **kwargs)

    def http_sessions(self, concurrency):
        """Return an HTTP session handler for a given concurrency model
        """
        if concurrency == models.THREAD_IO:
            return HttpClient(loop=new_event_loop())
        elif concurrency == models.ASYNC_IO:
            return self.http
        else:
            return GreenHttp(self.http)

    def flush_queues(self, *queues):
        return self.broker.flush_queues(*queues)

    def on_events(self, callback):
        self.pubsub.on_events(callback)

    def closing(self):
        return self._closing

    def close(self):
        '''Close this :class:`.TaskBackend`.

        Invoked by the :class:`.Actor` when stopping.
        '''
        if not self._closing:
            self._closing = True
            self.manager.close()

    def queue_task(self, jobname, callback=True, **kwargs):
        '''Try to queue a new :task

        :param callback: when true (default) return a future called back once
            the task done, otherwise it is called back once the task is queued.
        :return: a :class:`.Future` resulting in a task once finished or
            Nothing
        '''
        task = self._create_task(jobname, **kwargs)
        if task:
            future = self.broker.queue(task, callback)
            if self._loop.is_running():
                return self.green_pool.wait(future)
            else:
                return future

    def queue_task_local(self, jobname, **kwargs):
        kwargs['queue'] = self.node_name
        return self.queue_task(jobname, **kwargs)

    def execute_task(self, jobname, **kwargs):
        '''Execute a task immediately
        '''
        kwargs['queue'] = False
        kwargs['callback'] = True
        return self.queue_task(jobname, **kwargs)

    # INTERNALS
    def _create_task(self, jobname, meta_params=None, expiry=None, queue=True,
                     delay=None, **kwargs):
        '''Try to queue a new :ref:`Task`.

        This method returns a :class:`.Future` which results in the
        task ``id`` created. If ``jobname`` is not a valid
        :attr:`.Job.name`, a ``TaskNotAvailable`` exception occurs.

        :param jobname: the name of a :class:`.Job`
            registered with the :class:`.TaskQueue` application.
        :param meta_params: Additional parameters to be passed to the
            :class:`Task` constructor (not its callable function).
        :param expiry: optional expiry timestamp to override the default
            expiry of a task.
        :param kwargs: optional dictionary used for the key-valued arguments
            in the task callable.
        :return: a :class:`.Future` resulting in a task once finished or
            Nothing
        '''
        if self._closing:
            self.logger.warning('Cannot queue task, task backend closing')
            return
        if jobname in self.registry:
            job = self.registry[jobname]
            task_id = self.gen_unique_id()
            queued = time.time()
            if expiry is not None:
                expiry = get_time(expiry, queued)
            elif job.timeout:
                expiry = get_time(job.timeout, queued)
            meta_params = meta_params or {}
            if queue is not False:
                if queue is True:
                    queue = job.queue or self.cfg.default_task_queue
            else:
                queue = None
            return Task(task_id,
                        name=job.name,
                        queue=queue,
                        time_queued=queued,
                        expiry=expiry,
                        kwargs=kwargs,
                        status=states.QUEUED,
                        delay=delay,
                        **meta_params)
        else:
            raise TaskNotAvailable(jobname)
