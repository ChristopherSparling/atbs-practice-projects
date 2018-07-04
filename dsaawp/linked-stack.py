class LinkedStack:

    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,element,next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1
    
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        elem = self._head._element
        self._head = self._head._next
        self._size -= 1
        return elem

new_stack = LinkedStack()

for i in range(5):
    new_stack.push(i)
    print(new_stack.top())

for i in range(5):
    print(new_stack.pop())
