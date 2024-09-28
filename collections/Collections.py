from abc import ABC, abstractmethod


class ContainerADT(ABC):
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    @abstractmethod
    def add(self, e) -> None:
        pass

    @abstractmethod
    def remove(self, e) -> bool:
        pass

    @abstractmethod
    def contains(self, e) -> bool:
        pass

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    @abstractmethod
    def clear(self) -> None:
        pass


# NOTE: Here we define the Stack interface - how the stack collection should operate
class StackADT(ContainerADT):
    @abstractmethod
    def push(self, e: object) -> None:
        pass

    @abstractmethod
    def pop(self) -> object:
        pass

    @abstractmethod
    def top(self) -> object:
        pass

# NOTE: Here we define the Queue interface - how the queue collection should operate
class QueueADT(ContainerADT):
    @abstractmethod
    def enqueue(self, e: object) -> None:
        """Add an element to the end of the queue."""
        pass

    @abstractmethod
    def dequeue(self) -> object:
        """Remove and return the front element."""
        pass

    @abstractmethod
    def front(self) -> object:
        """Return the front element without removing it."""
        pass
    
class LinkedListBasedQueue(QueueADT):
    class _Node:
        def __init__(self, d, n=None):
            self._data = d
            self._next = n

    def __init__(self):
        self._size = 0
        self._first = None
        self._last = None

    def enqueue(self, e: object) -> None:
        """Add an element to the end of the queue."""
        new_node = LinkedListBasedQueue._Node(e)
        if self._size == 0:
            self._first = self._last = new_node
        else:
            self._first._next = new_node
        self._size += 1

    def dequeue(self) -> object:
        """Remove and return the front element."""
        if self._size == 0:
            return
        else:
            temp = self._first
            self._first = self._first._next
            self._size -= 1
            return temp

    def remove(self, e):
        if self._size == 0:
            return False
        temp = self._first
        if temp._data == e:
            self.dequeue()

        while temp:
            if temp._next and temp._next._data == e:
                temp._next = temp._next._next
                self._size -= 1
            if temp._next is None:
                self._last = temp
        return False


    def get_first(self) -> object:
        if self._size == 0:
            return None
        """Return the front element without removing it."""
        return self._first
    
    def get_last(self) -> object:
        if self._size == 0:
            return None
        """Return the front element without removing it."""
        return self._last


# NOTE: When implementing the stack using array as a base (static consequent memory), we choose the right
# side of the array to add and remove elements. This way the pop operation takes stable O(1) and the
# push operation takes amortized O(1) (asymptotic O(n))
class ArrayBasedStack(StackADT):
    def __init__(self, cap=10):
        super().__init__()
        self._capacity = 10
        self._arr = [None] * cap

    def _ensure_capacity(self):
        if self._size == self._capacity: # len(self._arr)
            new_arr = [None] * self._size * 2
            for i in range(self._size):
                new_arr[i] = self._arr[i]
            self._arr = new_arr
            self._capacity = self._capacity * 2

    def push(self, e: object) -> None:
        self._ensure_capacity()
        self._arr[self._size] = e
        self._size += 1

    def pop(self) -> object:
        if self._size == 0:
            return None
        top = self._arr[self._size - 1]
        self._arr[self._size - 1] = None
        self._size -= 1
        return top

    def top(self) -> object:
        if self._size == 0:
            return None
        top = self._arr[self._size - 1]
        return top

    def add(self, e) -> None:
        self.push(e)

    def remove(self, e) -> bool:
        pass

    def contains(self, e) -> bool:
        for i in range(self._size):
            if self._arr[i] == e:
                return True
        return False

    def clear(self) -> None:
        self._arr = [None] * self._capacity
        self._size = 0

    def __str__(self):
        s = ""
        for i in range(self._size):
            s += str(self._arr[i])
            if i != self._size - 1:
                s += "->"
        return s


# NOTE: When implementing the stack using linked data, we choose the front of the linked list
# to add and remove elements. This way the push and pop operations takes stable O(1)
# Note that we no more need to keep the references of both ends of the list, and just the front end is enough here
class LinkedListBasedStack(StackADT):
    class _Node:
        def __init__(self, d, n=None):
            self.data = d
            self.next = n

    def __init__(self):
        super().__init__()
        self._top = None

    def push(self, e: object) -> None:
        n = LinkedListBasedStack._Node(e, self._top)
        self._size += 1
        self._top = n

    def pop(self) -> object:
        if self._size == 0:
            return None
        top = self._top.data
        temp = self._top
        self._top = self._top.next
        temp.next = None
        self._size -= 1
        return top

    def top(self) -> object:
        if self._size == 0:
            return None
        else:
            return self._top.data

    def add(self, e) -> None:
        self.push(e)

    def remove(self, e) -> bool:
        pass

    def contains(self, e) -> bool:
        temp = self._top
        for i in range(self._size):
            if temp.data == e:
                return True
            temp = temp.next
        return False

    def clear(self) -> None:
        self._top = None
        self._size = 0

    # def __str__(self):
    #     s =


class ListADT(ContainerADT):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def first(self) -> object:
        pass

    @abstractmethod
    def last(self) -> object:
        pass

    @abstractmethod
    def get_element_at(self, index) -> object:
        pass

    @abstractmethod
    def add_element_at(self, e, index) -> object:
        pass

    @abstractmethod
    def remove_element_at(self, index) -> object:
        pass

    @abstractmethod
    def add_first(self, e) -> None:
        pass

    @abstractmethod
    def add_last(self, e) -> None:
        pass

    @abstractmethod
    def remove_first(self) -> object:
        pass

    @abstractmethod
    def remove_last(self) -> object:
        pass

    @abstractmethod
    def is_first(self) -> bool:
        pass

    @abstractmethod
    def is_first(self) -> bool:
        pass

    @abstractmethod
    def get_prev(self, e) -> object:
        pass

    @abstractmethod
    def get_next(self, e) -> object:
        pass


class ArrayBasedList(ListADT):
    def __init__(self, capacity=10):
        super().__init__()
        self._array = [None] * capacity

    # NOTE: Implementing the iter method in the ArrayBasedList class makes it iterable and
    # allows python to iterate over it using foreach loop
    # NOTE: We are using the DivisibleByNumber iterator here, to implement a simple
    # forward iterator for the Array Based List
    # if we pass the number as 1, then all elements of the list will be divisible by 1,
    # hence we'll have an iterator which iterates over all elements in list
    def __iter__(self):
        # The DivisibleByNumIterator receives the list on which the iteration should be performed
        # NOTE: if we pass it the original list, then the iterator will behave as lazy (fail fast)
        return ArrayBasedList.DivisibleByNumberIterator(self._array, self._size, 1)
        # NOTE: if we pass it the copy of the list, then it will behave as a snapshot iterator(fail safe)
        # return ArrayBasedList.DivisibleByNumberIterator(self._array[0: self._size], self._size, 1)

    # This iterator iterates over the elements of the ArrayBasedList if those are divisible by the num
    class DivisibleByNumberIterator:
        def __init__(self, arr, s, num):
            if num == 0:
                raise ValueError("Can not perform division to 0")
            self._cur_ind = 0
            # NOTE: We can receive a snapshot of the original array to iterate over, but we can also
            # receive the original array
            # In order to make this iterator 100% snapshot, we can always take a new snapshot of the array we receive
            # self._arr = [i for i in arr] snapshot
            self._arr = arr
            self._size = s
            self._n = num

        def __next__(self):
            temp_ind = self._cur_ind
            while temp_ind < self._size:
                if self._arr[temp_ind] % self._n == 0:
                    self._cur_ind = temp_ind + 1
                    return self._arr[temp_ind]
                temp_ind += 1
            raise StopIteration

    # NOTE: While the __iter__ method provides the default iterator for the iterable object (ArrayBasedList here),
    # there are usually more options to iterate over the same collection, like backwards iteration, selective iteration, etc
    # This is why to be able to perform other types of iterations, we create methods which returns respective iterator objects
    def divisible_by_num_iter(self, num):
        return ArrayBasedList.DivisibleByNumberIterator(self._array[0: self._size], self._size, num)

    def reverse(self): # O(n)
        for i in range(self._size // 2):
            self._array[i], self._array[self._size - 1 - i] = \
                self._array[self._size - 1 - i], self._array[i]

    def add_element_at(self, e, index) -> object:
        pass

    def add_from_back(self, e):
        self._array[self._size] = e
        self._size += 1
    # def __getitem__(self, item): # O(1)
    #     if item < 0 or item >= self._size:
    #         raise IndexError("ArrayBasedList index is out of range")
    #     return self._array[item]
    #
    # def __setitem__(self, key, value): # O(1)
    #     if key < 0 or key >= self._size:
    #         raise IndexError("ArrayBasedList index is out of range")
    #     self._array[key] = value

    def remove_element_at(self, index) -> object:
        if self._size == 0 or index >= self._size:
            return
        for i in range(index, self._size):
            self._array[i] = self._array[i+1]
            self._array[self._size - 1] = None
        self._size -= 1

    def is_first(self) -> bool:
        pass

    def get_prev(self, e) -> object:
        pass

    def get_next(self, e) -> object:
        pass

    # ) You are given a list of positions. Create an instance method that removes all the
    # items from the ArrayList corresponding to those positions
    def remove_elements_at_positions(self, positions: list):
        positions = sorted(positions)
        count = 0
        for index in positions:
            self.remove_element_at(positions[index - count])
            self._size -= 1 
            count += 1

    # Create an instance method that removes all duplicates from the ArrayList
    def remove_duplicates(self):# O(n)
        distinct_values = ArrayBasedList()
        for el in self._array:
            if el not in distinct_values:
                distinct_values.add_from_back(el)  
        self._array = distinct_values
        self._size = len(self._array)

    def print(self): # O(n)
        print("[", end="")
        for i in range(self._size - 1):
            print(self._array[i], end=", ")
        if self._size > 0:
            print(self._array[self._size - 1], end="")
        print("]")

    def __str__(self): # O(n)
        s = "["
        for i in range(self._size - 1):
            s += str(self._array[i]) + ", "
        if self._size > 0:
            s += str(self._array[self._size - 1])
        s += "]"
        return s

    def first(self) -> object: # O(1)
        if self._size == 0:
            return None
        return self._array[0]

    def last(self) -> object: # O(1)
        if self._size == 0:
            return None
        return self._array[self._size - 1]

    def get_element_at(self, index) -> object: # O(1)
        if index >= self._size:
            return None
        return self._array[index]

    def add_first(self, e) -> None: # O(n)
        if self._size == len(self._array):
            self._resize()
        for i in range(self._size, 0, -1):
            self._array[i] = self._array[i - 1]
        self._array[0] = e
        self._size += 1

    def _resize(self): # O(n)
        n = [None] * self._size * 2
        for i in range(self._size):
            n[i] = self._array[i]
        self._array = n

    def add_last(self, e) -> None: # O(n)
        if self._size == len(self._array):
            self._resize()
        self._array[self._size] = e
        self._size += 1

    def remove_first(self) -> object: # O(n)
        if self._size == 0:
            return None
        t = self._array[0]
        for i in range(0, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return t

    def remove_last(self) -> object: # O(1)
        if self._size == 0:
            return None
        t = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return t

    def add(self, e) -> None: # O(n)
        self.add_last(e)

    def remove(self, e) -> bool: # O(n)
        for i in range(self._size):
            if e == self._array[i]:
                self._array[i] = None
                for j in range(i, self._size - 1):
                    self._array[j] = self._array[i + 1]
                self._size -= 1
                return True
        return False

    def contains(self, e) -> bool: # O(n)
        for i in range(self._size):
            if e == self._array[i]:
                return True
        return False

    def is_empty(self) -> bool: # O(1)
        return self._size == 0

    def clear(self) -> None:
        pass

class LinkedList(ListADT):
    class _DataWrapper:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        super().__init__()
        self._first = None
        self._last = None
        self._current = self._first

    def add_element(self, el):
        new_node = LinkedList._DataWrapper(el)
        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._size += 1

    def _reverse_rec_helper(self, curr):  # O(n)
        if not curr:
            return
        temp = curr.next
        self._reverse_rec_helper(curr.next)
        if temp:
            temp.next = curr

    def reverse_rec(self): # O(n)
        self._reverse_rec_helper(self._first)
        self._first.next = None
        self._first, self._last = self._last, self._first

    def reverse_optimized(self): # O(n)
        prev = None
        curr = self._first
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self._first, self._last = self._last, self._first

    def reverse(self): # O(n2)
        front_pointer = self._first
        for i in range(self._size // 2):
            back_pointer = self._first
            for j in range(self._size - 1 - i):
                back_pointer = back_pointer.next
            front_pointer.data, back_pointer.data = back_pointer.data, front_pointer.data
            front_pointer = front_pointer.next

    def remove_duplicates(self):
        distinct_values = LinkedList()
        current = self._first
        while current:
            if current.data not in distinct_values:
                distinct_values.add_element(current.data)
            if current.next != None:
                    current = current.next 
        self._first = distinct_values._first
        self._last = distinct_values._last
        self._size = distinct_values._size
            

    # NOTE: The LinkedList snapshot iterator creates a copy/snapshot of the given linked list in a python list object
    # and then performs the iteration on that object
    class LinkedListSnapshotIterator:
        def __init__(self, n):
            self._snapsh = []
            temp = n
            while temp:
                self._snapsh.append(temp.data)
                temp = temp.next
            self._ind = 0

        def __next__(self):
            if self._ind == len(self._snapsh):
                raise StopIteration
            ind = self._ind
            self._ind += 1
            return self._snapsh[ind]

    class DivisibleByNumberIterator:
        def __init__(self, node, num):
            if num == 0:
                raise ValueError("Can not perform division to 0")
            self._cur = node
            self._n = num

        def __next__(self):
            temp = self._cur
            while temp:
                if temp.data % self._n == 0:
                    self._cur = temp.next
                    return temp.data
                temp = temp.next
            raise StopIteration

    # NOTE: While the __iter__ method provides the default iterator for the iterable object (LinkedList here),
    # there are usually more options to iterate over the same collection, like backwards iteration, selective iteration, etc
    # This is why to be able to perform other types of iterations, we create methods which returns respective iterator objects
    def divisible_by_num_iter(self, num):
        return LinkedList.DivisibleByNumberIterator(self._first, num)

    # NOTE: Another method returning a snapshot iterator for LinkedList
    def snapshot_iter(self):
        return LinkedList.LinkedListSnapshotIterator(self._first)

    # NOTE: Making the LinkedList iterable here and implementing the iterator in the linkedList itself,
    # thus making the LinkedList an iterator as well
    def __iter__(self):
        # NOTE: The linkedList should have a self property to help it perform the iteration over itself
        # whenever it is treated as an iterator object (in for loop)
        # This property will be initialized with the list first node each time list iterator is created
        self._cur = self._first
        return self

    # NOTE: This makes the LinkedList object an iterator
    def __next__(self):
        if self._cur == None:
            raise StopIteration
        temp = self._cur
        self._cur = self._cur.next
        return temp.data

    # def __getitem__(self, item): # O(n)
    #     if item < 0 or item >= self._size:
    #         raise IndexError("LinkedList index is out of range")
    #     temp = self._first
    #     while item:
    #         temp = temp.next
    #         item -= 1
    #     return temp.data
    #
    # def __setitem__(self, key, value): # O(n)
    #     if key < 0 or key >= self._size:
    #         raise IndexError("LinkedList index is out of range")
    #     temp = self._first
    #     while key:
    #         temp = temp.next
    #         key -= 1
    #     temp.data = value

    def is_first(self) -> bool:
        pass

    def get_prev(self, e) -> object:
        pass

    def get_next(self, e) -> object:
        pass

    def first(self) -> object: # O(1)
        if self._size == 0:
            return None
        return self._first.data

    def last(self) -> object: # O(1)
        if self._size == 0:
            return None
        return self._last.data

    def get_element_at(self, index) -> object: # O(1)
        if index < 0 or index >= self._size:
            raise IndexError
        t = self._first
        for i in range(index):
            t = t.next
        return t.data

    def add_element_at(self, e, index) -> object: # O(n)
        if index < 0 or index >= self._size:
            raise IndexError
        if index == 0:
            self.add_first(e)
            return
        t = self._first
        for i in range(index - 1):
            t = t.next
        n = LinkedList._DataWrapper(e, t.next)
        t.next = n
        self._size += 1

    def remove_element_at(self, index) -> object: # O(n)
        if index < 0 or index >= self._size:
            raise IndexError
        if index == 0:
            self._first = self._first.next
            self._size -= 1
            return
        t = self._first
        for i in range(index - 1):
            t = t.next
        t.next = t.next.next
        if index == self._size - 1:
            self._last = t
        self._size -= 1

    def add_first(self, e) -> None: # O(1)
        # Option 1
        d = LinkedList._DataWrapper(e, self._first)
        # Option 2
        # d = LinkedList.DataWrapper(e)
        # d.next = self._first
        self._size += 1
        self._first = d
        if self._size == 1:
            self._last = d

    def add_last(self, e) -> None: #O(1)
        d = LinkedList._DataWrapper(e)
        if self._size == 0:
            self._first = d
            self._last = d
        else:
            self._last.next = d
            self._last = d
        self._size += 1

    def remove_first(self) -> object:
        if self._size == 0:
            return None
        temp = self._first
        if self._size == 1:
            self._first = self._last = None
        else:
            self._first = self._first.next
            temp.next = None
        self._size -= 1
        return temp.data

    def remove_last(self) -> object: # O(n)
        if self._size == 1:
            self._size = 0
            self._first = self._last = None
            return
        t = self._first
        while t:
            if t.next == self._last:
                self._last = t
                self._size -= 1
                self._last.next = None
            t = t.next

    def __str__(self):
        s = ""
        t = self._first
        while t:
            s += "(" + str(t.data) + ")"
            if t.next:
                s += "->"
            t = t.next
        return s

    def print(self): # O(n)
        t = self._first
        print("LinkedList: ", end='')
        while t:
            print("(", t.data, ")", end='')
            if t.next:
                print("->", end='')
            t = t.next
        print()

    def add(self, e) -> None:
        pass

    def remove(self, e) -> bool:
        pass

    def contains(self, e) -> bool:
        pass

    def is_empty(self) -> bool:
        pass

    def clear(self) -> None:
        self._size = 0
        self._first = self._last = None


class DoubleLinkedList(ListADT):
    def first(self) -> object:
        pass

    def last(self) -> object:
        pass

    def get_element_at(self, index) -> object:
        pass

    def add_element_at(self, e, index) -> object:
        pass

    def remove_element_at(self, index) -> object:
        pass

    def add_first(self, e) -> None:
        pass

    def add_last(self, e) -> None:
        pass

    def remove_first(self) -> object:
        pass

    def remove_last(self) -> object:
        if self._size == 0:
            return None
        t = self._last
        self._last = self._last.prev
        self._last.next = None
        self._size -= 1
        return t.data

    def is_first(self) -> bool:
        pass

    def get_prev(self, e) -> object:
        pass

    def get_next(self, e) -> object:
        pass

    def add(self, e) -> None:
        pass

    def remove(self, e) -> bool:
        pass

    def contains(self, e) -> bool:
        pass

    def clear(self) -> None:
        pass

    class _DataWrapper:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        super().__init__()
        self._first = None
        self._last = None