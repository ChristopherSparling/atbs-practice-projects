class CircularQueue:

    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element,next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1
    
    def first(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        prev_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = prev_head._next
        self._size -= 1
        return prev_head._element 

    def enqueue(self,element):
        new_node = self._Node(element,None)
        if self.is_empty():
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
    
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

new_stack = CircularQueue()

for i in range(5):
    new_stack.enqueue(i)
    print(new_stack.first())

for i in range(5):
    print(new_stack.dequeue())