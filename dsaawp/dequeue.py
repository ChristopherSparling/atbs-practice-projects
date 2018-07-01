class  Dequeue:
    """Double-ended Queue"""
    DEFAULT_CAPACITY = 5
    
    def __init__(self):
        self._data = [None] * Dequeue.DEFAULT_CAPACITY
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

    def last(self):
        back = (self._front + self._size - 1) % len(self._data)
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[back]

    def delete_first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        elem = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        self._print()
        return elem

    def delete_last(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        elem = self._data[back]
        self._data[back] = None
        self._size -= 1
        self._print()
        return elem

    def add_first(self, elem):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        
        self._front = (self._front - 1) % len(self._data) # shift _front one earlier, which must be available
        self._data[self._front] = elem
        self._size += 1
        print("Front: ", self._front)
        self._print()

    def add_last(self, elem):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        back = (self._front + self._size) % len(self._data)
        print("Front: ", self._front)
        print("Back: ", back)
        self._data[back] = elem
        self._size += 1
        self._print()

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
        walk = self._front
        for i in range(self._size):
            print(self._data[walk], end = ' ')
            walk = (1 + walk) % len(self._data)
        print()

new_dequeue = Dequeue()

new_dequeue.add_first('a')
new_dequeue.add_first('b')
new_dequeue.add_last('c')
new_dequeue.add_last('a')

new_dequeue.delete_first()
new_dequeue.delete_last()
new_dequeue.delete_first()
new_dequeue.delete_last()
