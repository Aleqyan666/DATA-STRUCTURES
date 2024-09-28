from abc import ABC, abstractmethod

class Collection(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def empty(self) -> None:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

class List(Collection):
    @abstractmethod
    def add_first(e: object):
        pass

    @abstractmethod
    def remove_first()-> bool:
        pass

    @abstractmethod
    def add_last(e: object) -> None:
        pass

    @abstractmethod
    def remove_last()-> bool:
        pass

    @abstractmethod
    def first()-> object:
        pass

    @abstractmethod
    def last() -> object:
        pass

    @abstractmethod
    def replace(e: object, r: object)-> bool: # replaces the first occurrence of e in List with r and returns true
        pass

    @abstractmethod
    def add_at(e: object, index: int) -> bool:
        pass
    
    @abstractmethod
    def get_at(index: int) -> object:
        pass

    @abstractmethod
    def remove_at(index: int) -> object:
        pass

class Stack(Collection):
    @abstractmethod
    def push(e: object) -> None:
        pass

    @abstractmethod
    def pop() -> object:
        pass

    @abstractmethod
    def top() -> object:
        pass

class MyStack(Stack):
    def push(e: object) -> None:
        #!
        pass

    def pop() -> object:
        #!
        pass

    def top() -> object:
        #!
        pass

class LinkedList(List):
    class Node:
        def __init__(self, data, next=None):
            self.next = next
            self.data = data

    def __init__(self):
        self._size = 0
        self._first = None
        self._last = None

    class LinkedListOddPositionIterator:
        def __init__(self, start_node):
          self.current_node = start_node
          self.ind = 0

        def __iter__(self):
          return self
        
        def __next__(self):
            if self.current_node is None:
                raise StopIteration

            if self.ind % 2 == 0:  
                self.current_node = self.current_node.next
                self.ind += 1

            if self.current_node is None:  
                raise StopIteration

            temp = self.current_node.data
            self.current_node = self.current_node.next
            self.ind += 1  
            return temp
              
    def odd_position_iterator(self):
            return LinkedList.LinkedListOddPositionIterator(self._first)

    def add_first(self, e) -> None:
        new_node = LinkedList.Node(e)
        if self._size == 0:
            self._first = new_node
            self._last = new_node
        else:
            new_node.next = self._first
            self._first - new_node
        self._size += 1

#     Implement both a recursive and an iterative remove_duplicates() method for
# the LinkedList class. These methods should remove duplicates from the
# sorted singly linked list, such that each element appears only once.
    def remove_duplicates(self):
        unique_values = LinkedList()
        if self._size == 0 or self._size == 1 or self._first == None:
            return
        
        current =  self._first
        while current:
            if not unique_values.contains(current.data):
                unique_values.add_last(current.data)
            else:
                current = current.next
            self._size = unique_values._size
            self._first = unique_values._first
            self._last = unique_values._last
            return unique_values

    def add_last(self, e: object) -> None:
        new_node = LinkedList.Node(e)
        if self._size == 0:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._size += 1

    def remove_first(self) -> bool:
        if self._size == 0:
            return False
        if self._size == 1:
            self._first = None
            self._last = None
            return True
        else:
            self._first = self._first.next
        self._size -= 1

    def remove_last(self) -> bool:
        if self._size == 0:
            return False
        if self._size == 1:
            self._first = None
            self._last = None
        else:
            current = self._first
            while current != self._last:
                current = current.next 
            current.next = None            
            self._last = current        
        self._size -= 1
        return True
    
    def contains(self, obj: object):
        if self._size == 0:
            return False
        current = self._first
        while current:
            if current.data == obj:
                return True
            current = current.next
        return False
            

    def first(self) -> object:
        return self._first

    def last(self) -> object:
        return self._last
    
    def add_at(self, index: int, e: object) -> None:
        pass
    
    def empty(self) -> None:
        pass
    
    def get_at(self, index: int) -> object:
        pass
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def remove_at(self, index: int) -> bool:
        pass
    
    def replace(self, index: int, e: object) -> bool:
        pass
    
    def size(self) -> int:
        return self._size

#     Implement both a recursive and 
# an iterative add_before(el: object, n: object) method for
#  the LinkedList class. These methods should add the n
# object to the LinkedList before the first occurrence of the el object.
    def add_before(self, el: object, new: object):
        current = self._first

        if self._size == 0 or self._first is None:
            return
        
        if self._first.data == el:
            new_node = LinkedList.Node(new)
            new_node.next = self._first
            self._first = new_node
            self._size += 1
            return
        
        while current.next:
            if current.next.data == el:
                new_node.next = current.next
                current.next = new_node
                self._size += 1
                return
            current = current.next

        
    
    def recursive_add_before(self, el: object, new: object, current=None): #!DO IT AGAIN MYSELF
        if self._first is None or self._size == 0:
            return
        
        if self._first == el and self._size == 1:
            new_node = LinkedList.Node(el)
            new_node.next = self._first
            self._first = new_node
            self._size += 1
            return

        if current is None:
            current = self._first

        if current.next ==  el:
            new_node =  LinkedList.Node(el)
            new_node.next = current.next
            current.next = new_node
            self._size += 1

        if current.next is not None:
            self.recursive_add_before(el, new, current.next)


#     Implement both a recursive and an iterative add_after(el: object, n:
# object) method for the LinkedListStack class. These methods should add
# the n object to the LinkedListStack after the first occurrence of the el object.
    def add_after(self, el: object, new: object):
        if self._size == 0 or self._first is None:
            return
        
        current = self._first
        
        while current:
            if current.data == el:
                new_node = LinkedList.Node(new)
                new_node.next = current.next
                current.next = current.next
                self._size += 1
                break

            current = current.next


    def recursive_add_after(self, el: object, new: object):
        #!
        pass


    class LinkedListForwardIterator:
        def __init__(self, start_node):
            self.current_node = start_node

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current_node is None:
                raise StopIteration
            data = self.current_node.data
            self.current_node = self.current_node.next
            return data
        
    def __iter__(self):
      return LinkedList.LinkedListForwardIterator(self._first)
      
    
class DoubleLinkedList(List):
    class Node:
        def __init__(self, data, next=None, prev=None):
          self.data = data
          self.prev = None
          self.next = None

    def __init__(self):
      self._size = 0
      self._first = None
      self._last = None

    def add_first(self, e) -> None:
        new_node = LinkedList.Node(e)
        if self._size == 0:
            self._first = new_node
            self._last = new_node
        else:
            new_node.next = self._first
            self._first.prev = new_node
            self._first = new_node
        self._size += 1

    def add_last(self, e: object) -> None:
        new_node = LinkedList.Node(e)
        if self._size == 0:
            self._first = new_node
            self._last = new_node
        else:
            new_node.prev = self._last
            self._last.next = new_node
            self._last = new_node
        self._size += 1

    def remove_first(self) -> bool:
        if self._size == 0:
            return False
        if self._size == 1:
            self._first = None
            self._last = None
            return True
        else:
            self._first = self._first.next
            self._first.prev = None
        self._size -= 1
        return True

    def remove_last(self) -> bool:
        if self._size == 0:
            return False
        if self._size == 1:
            self._first = None
            self._last = None
        else:
            self._last = self._last.prev  
            self._last.next = None      
        self._size -= 1
        return True
    
    def first(self) -> object:
        if self._first is not None:
            return self._first.data
        return None

    def last(self) -> object:
        if self._last is not None:
            return self._last.data
        return None

class ArrayList(List):
    def __init__(self, capacity=10):
      self._size = 0
      self._arr = [None] * capacity


    # Implement odd position iterators for the LinkedList and
    #  ArrayList classes (the iterators should go only over 
    # elements under odd indexes, like 1, 3, 5, ... .
    # E.g for [21, 32, 33, 78, 49, 51] list, 
    # the odd position iterator should iterate over 32,
    # 78 and 51 elements only.


    class ArrayListOddPositionIterator:
        def __init__(self, array, size):
            self.array = array
            self.size = size
            self.current = 1 if self.size > 0 else self.size

        def __iter__(self):
          return self

        def __next__(self):
            if self.current >= self.size:
                raise StopIteration 
            temp = self.array[self.current]
            self.current += 2
            return temp
        
    def odd_position_iterator(self):
        return ArrayList.ArrayListOddPositionIterator(
            self._arr, self._size)
    
    def _resize(self):
        new_arr = [None] * self._size * 2 # also can * by self._capacity
        for i in range(self._size):
            new_arr[i] = self._arr[i]
        self._arr = new_arr
    
    def reverse(self):
        for i in range(self._size):
            self._arr[i], self._arr[self._size - i - 1] = \
                self._arr[self._size - i -1], self._arr[i]
            
    def add_from_back(self, e):
        if self._size == len(self._arr):
            self._resize()
        self._arr[self._size] = e
        self._size += 1 

    def remove_first(self) -> object:
        if self._size == 0:
            return None
        first_element = self._arr[0]
        for i in range(self._size - 1):
            self._arr[i] = self._arr[i + 1]
        self._arr[self._size - 1] = None
        self._size -= 1
        return first_element
    
    def remove_last(self) -> object:
        if self._size == 0:
            return None
        last_element = self._arr[self._size - 1]
        self._arr[self._size - 1] = None
        self._size -= 1
        return last_element
    
    def remove(self, e) -> bool:
        if self._size == 0:
            return False
        for i in range(self._size):
            if self._arr[i] == e:
                for j in range(i, self._size - 1):
                    self._arr[j] = self._arr[j + 1]
                self._size -= 1
                return True
        return False
    
    def contains(self, e) -> bool:
        for i in range(self._size):
            if self._arr[i] == e:
                return True
        return False
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def get_element_at(self, index) -> object:
        if index < self._size:
            return None
        return self._arr[index]
    
#     Implement find_max_consecutive_ones() instance method for the
# ArrayList class that returns the maximum
#  number of consecutive 1's in the array.
#  Consider that all items in the ArrayList are either 1 or 0.
    def find_max_consecutive_ones(self) -> int:
        if self._size == 0:
            return 0
        count, answer = 0
        for i in range(self.size):
            if self._arr[i] == 1:
                count += 1
                if count > answer:
                    answer = count
            else: 
                count = 0
        return answer
    
    def add_at(self, index, e):
        pass

    def add_first(self, e):
        pass

    def add_last(self, e):
        pass

    def empty(self):
        pass

    def first(self):
        pass

    def get_at(self, index):
        pass

    def last(self):
        pass

    def remove_at(self, index):
        pass

    def replace(self, index, e):
        pass

    def size(self):
        pass
    
class LinkedListBasedStack(Stack):
    class _Node:
        def __init__(self, data, next=None):
          self.data = data
          self.next = next
    
    def __init__(self):
      self._size = 0
      self._top = None

    def push(self, e: object) -> None:
        new_node = LinkedListBasedStack._Node(e, self._top)
        self._size += 1
        self._top = new_node

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
        return self._top.data

    def add_after(self, el: object, new: object):
        if self._size == 0 or self._top is None:
            return
        
        current = self._top

        while current:
            if current.data == el:
                new_node = LinkedListBasedStack._Node(new)
                new_node.next =  current.next
                current.next = new_node
                self._size += 1
                break
            else:
                current = current.next

    def add_after_recursive(self, el: object, new: object, current=None):
        if self._size == 0 or self._top is None:
            return
        
        if current is None:
            return

        if current.data == el:
            new_node = LinkedListBasedStack._Node(new)
            new_node.next = current.next
            current.next = new_node
            self._size += 1
        
        self.add_after_recursive(el, new, current.next)


    
    def empty(self) -> None:
        pass
    
    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass

    def __iter__(self):
        return self.LinkedListBasedStackForwardIterator(self._top)

    class LinkedListBasedStackForwardIterator:
        def __init__(self, top_node):
          self.current_node = top_node

        def __iter__(self):
          return self
        
        def __next__(self):
            if self.current_node is None:
              raise StopIteration
            data = self.current_node.data
            self.current_node = self.current_node.next
            return data


class Queue(Collection):
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

class LinkedListBasedQueue(Queue):
    class _Node:
        def __init__(self, data, next=None):
          self._data = data
          self._next = next

    def __init__(self):
      self._first = None
      self._last = None
      self._size = 0

    def enqueue(self, e: object) -> None:
        """Add an element to the end of the queue."""
        new_node = LinkedListBasedQueue._Node(e)

        if self._size == 0:
            self._first = self._last = new_node
        else:
            self._last._next = new_node
            self._last = new_node
        self._size += 1

    def dequeue(self) -> object:
        """Remove and return the front element."""
        if self._first is None or self._size == 0:
            return None
        
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
            return True  

        while temp and temp._next:
            if temp._next._data == e:
                if temp._next == self._last:
                    self._last = temp
                temp._next = temp._next._next
                self._size -= 1
                return True  
            
            temp = temp._next

        return False  




    def get_first(self) -> object:
        """Return the front element without removing it."""
        return self._first
    
    
    def get_last(self) -> object:
        """Return the front element without removing it."""
        return self._last


# Odd position iterator for linkedList
# llist = LinkedList()
# llist.add_last(1)
# llist.add_last(2)
# llist.add_last(3)
# llist.add_last(4)

# iteratorlinked = LinkedList.odd_position_iterator(llist)
# for el in iteratorlinked:
#     print(el)

# Odd position iterator for ArrayList
# alist = ArrayList()
# alist.add_from_back(1)
# alist.add_from_back(2)
# alist.add_from_back(3)
# alist.add_from_back(4)

# iterator = ArrayList.odd_position_iterator(alist)
# for el in iterator:
#     print(el)

        
# stack = LinkedListBasedStack() option 1

# # Push some elements onto the stack
# stack.push(1)
# stack.push(2)
# stack.push(3)

# # Iterate through the stack using a for loop
# for element in stack:
#     print(element)


# stack = LinkedListBasedStack() option 2

# iterator = iter(stack)

# try: 
#     while True:
#         print(next(iterator))
# except StopIteration:
#     pass

