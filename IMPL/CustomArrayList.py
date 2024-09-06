from EXCEPTIONS import OutOfBoundsException

class ArrayList:

    def __init__(self, initial_capacity=10) -> None:
        self._capacity = initial_capacity
        self._size = 0
        self._elements = [None] * initial_capacity

    def __len__(self) -> int:
        return self._size
    
    def _resize(self) -> None:
        self._capacity *= 2
        new_elements = [None] * self._capacity
        for i in range(self._size):
            new_elements[i] = self._elements[i]
        self._elements = new_elements

    def add_last(self, element) -> None:
        #checking if there's need to enlarge the list if and only if the capacity is full
        if self._size == self._capacity:
            self._resize()
        self._elements[self._size] = element
        self._size += 1

    def add_first(self, element) -> None:
        #checking if there's need to enlarge the list if and only if the capacity is full
        if self._size == self._capacity:
            self._resize()
        for i in range (self._size - 1, 0, -1):
            self._elements[i] = self._elements[i-1] 
        self._elements[0] = element
        self._size += 1

    def get(self, index):
        if index >= 0 and index < self._size:
            return self._elements[index]
        else:
            raise OutOfBoundsException(self, index)

    def remove(self, index):
        if index >= 0 and index < self._size:
            for i in range(index, self._size - 1):
                self._elements[i] = self._elements[i + 1]
            self._elements[self._size - 1] = None
            self._size -= 1
        else:
            raise OutOfBoundsException(self, index)