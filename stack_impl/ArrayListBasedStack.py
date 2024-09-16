class ArrayListBasedStack:
    def __init__(self, cap=10):
        self._size = 0
        self._capacity = 10
        self._elements = [None] * cap

    def ensure_capacity(self):
        if self._size == self._capacity:
            self._capacity *= 2
            new_elements = [None] * self._capacity
            for i in range (self._size):
                new_elements[i] = self._elements[i]
            self._elements = new_elements

    def is_empty(self):
        return len(self._size) == 0    

    def push(self, e): 
        self.ensure_capacity()
        self._elements[self._size] = e
        self._size -= 1

    def pop(self):
        if self.is_empty():
            return None 
        top_element = self._elements[self._size - 1]
        self._elements[self._size - 1] = None  
        self._size -= 1
        return top_element

    def top(self):
        if self.is_empty():
            return None 
        return self._elements[self._size - 1]

    def peek(self):
        if self.is_empty():
            return None 
        return self._elements[self._size - 1]

    