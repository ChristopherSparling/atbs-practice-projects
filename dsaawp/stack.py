class Stack:
    """Basic LIFO Stack"""

    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, elem):
        self._data.append(elem)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()
    


new_stack = Stack()

for i in range(5):
    new_stack.push(i)
    print("Length of Stack: ", new_stack.__len__())
    print("Top of Stack: ", new_stack.top())


print("\nAll elements:")
for i in range(new_stack.__len__()):
    print(new_stack.pop())