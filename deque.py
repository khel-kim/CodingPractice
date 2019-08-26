import queue as module_queue
queue = module_queue.Queue()
queue.put(10)
queue.get()

Q = queue.queue
Q.append(10)
Q.popleft()