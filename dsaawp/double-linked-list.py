class DoubleLinkedList:

    class _DoubleNode:
        __slots__ = '_element','_next', '_last'
        def __init__(self,element,next_node, last_node):
            self._element = element
            self._next = next_node
            self._last = last_node

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def push_head(self, element):
        self._head = self._DoubleNode(element, self._head, None)
        if self._size > 0:
            self._head._next._last = self._head
        else:
            self._tail = self._head
        self._size += 1
    
    def push_tail(self, element):
        self._tail = self._DoubleNode(element,None,self._tail)
        if self._size > 0:
            self._tail._last._next = self._tail
        else: 
            self._head = self._tail
        self._size += 1
    
    def top(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self._head._element
    
    def bottom(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self._tail._element

    def pop_head(self):
        if self.is_empty():
            raise Exception('List is empty')

        self._size -= 1
        elem = self._head._element
        self._head = self._head._next
        
        # Catches case of one element in list
        if self._size > 0:
            self._head._last = None
        
        return elem 

    def pop_tail(self):
        if self.is_empty():
            raise Exception('List is empty')

        self._size -= 1
        elem = self._tail._element
        self._tail = self._tail._last
        if self._size > 0:
            self._tail._next = None
        
        return elem

new_stack = DoubleLinkedList()

for i in range(5):
    new_stack.push_head(i)
    print("Top: ", new_stack.top(), " Bottom: ", new_stack.bottom())
    new_stack.push_tail(i)
    print("Top: ", new_stack.top(), " Bottom: ", new_stack.bottom())

for i in range(5):
    print(new_stack.pop_head())
    print(new_stack.pop_tail())
