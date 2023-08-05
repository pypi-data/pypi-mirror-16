from gevent import monkey
monkey.patch_all()

import gevent.pool
import gevent.queue

class asynchronizer():
    def __init__(self,workers):
        # workers define how many concurrent functions should be run
        self.workers = workers
        self.pool = gevent.pool.Pool(self.workers)
        self.pqueue = gevent.queue.PriorityQueue()

    def add(self,priority,func,*args,**kwargs):
        # this function adds other functions to the priority queue
        self.pqueue.put_nowait((priority,func,args,kwargs))

    def updateWorkers(self,workers):
        # can be used to update no. of workers if run() isn't called
        self.workers = workers
        self.pool = gevent.pool.Pool(self.workers)

    def run(self):
        # this function starts the gevent pool
        # this is a blocking function, so should be called last
        while not self.pqueue.empty() and not self.pool.full():
            for x in range(0,min(self.pqueue.qsize(),self.pool.free_count())):
                p,func,args,kwargs = self.pqueue.get_nowait()
                self.pool.start(self.pool.spawn(func,*args,**kwargs))
            self.pool.join()

a = asynchronizer(32)

def asynchronize(func):
    def converted_func(*args,**kwargs):
        priority = kwargs['priority']  if 'priority' in kwargs else 1

        # remove these two parameters , as they are used in add()
        # temporary fix
        if 'priority' in kwargs: del kwargs['priority']
        if 'func' in kwargs: del kwargs['func']

        a.add(priority,func,*args,**kwargs)
    return converted_func

def startPool():
    # wrapper for asynchronizer.run()
    a.run()

def setWorkers(workers):
    # wrapper for asynchronizer.updateWorkers()
    a.updateWorkers(workers)
