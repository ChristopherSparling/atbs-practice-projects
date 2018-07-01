class  Queue:
    """Basic FIFO Queue"""
    DEFAULT_CAPACITY = 5
    
    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        elem = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return elem

    def enqueue(self, elem):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = elem
        self._size += 1

    def _resize(self, new_cap):
        old = self._data
        self._data = [None] * new_cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
        print('Resize Triggered')

    def _print(self):
        for i in range(self._size):
            if self._data[self._front + i] != None:
                print(self._data[self._front + i], end = ' ')
        print()

new_queue = Queue()

for i in range(10):
    new_queue.enqueue(i)
    new_queue._print()

for i in range(10):
    new_queue.dequeue()
    new_queue._print()