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


    class StepIterator:
        def __init__(self, step: int , start_node):
            if step <= 0:
                raise ValueError
            self.step = step
            self.current_node = start_node

        def __iter__(self):
            return self

        def __next__(self):
            temp = self.current_node.data
            i = 0
            while i < self.step:
                if self.current_node is None:
                    raise StopIteration
                self.current_node = self.current_node.next
                i += 1
            return temp

    # Default iterator, 1-step iteration
    def __iter__(self):
        return self.StepIterator(1, self._first)

    def step_iterator(self, step):
        return self.StepIterator(step, self._first)

    
    # Given a list consisting only of 0s, 1s, and 2s, sort it so
    #  that all the 0s come first, followed by all the 1s, and then all the 2s.
    def sort_list(self):

        c0,  c1, c2 = 0
        if self._first is None:
           return None
        if self._size == 0 or self._size == 1:
            return None 

        current = self._first
        while current:
            if current.data == 0:
               c0 += 1
            if current.data == 1:
               c1 += 1
            if current.data == 2:
               c2 += 1
            current = current.next    
        
        self._first = self._last = None
        self._size = 0

        while c1 > 0:
            self.add_first(1)
            c1 -= 1

        while c0 > 0:
            self.add_first(0)
            c0 -= 1

        while c2 > 0:
            self.add_last(2)
            c2 -= 1     

            

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

    # Implement a method find_middle() that returns the middle node of the linked list.
    #  If the list has an even number of nodes, return the second middle node.
    def middle_node(self):
        if self._size == 0:
            return
        
        if self._size == 1:
            return self._first
    
        if self._size == 2:
            return self._last

        slow = self._first
        fast = self._first

        while fast:
            slow = slow.next
            fast = fast.next.next

        return slow

    
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


    def insert_before_max(self, el):
        new_node = LinkedList.Node(el)
        if self._size == 0:
            self._first = self._last = new_node
            self._size += 1
            return

        max = self._first.data
        current = self._first
        
        while current:
            if current.data > max:
                max = current.data
            current = current.next
        
        if self._first.data == max:
            new_node.next = self._first
            self._first = new_node
            self._size += 1 
            return

        previous = None
        curr = self._first
        while curr:
            if curr.data == max:
                new_node.next = curr
                previous.next = new_node
                self._size += 1
                break
            curr = curr.next
            previous = previous.next
        

    
    def recursive_add_before(self, el: object, new: object, current=None):
        if self._first is None or self._size == 0:
            return
        
        if self._first.data == el and self._size == 1:
            new_node = LinkedList.Node(new)
            new_node.next = self._first
            self._first = new_node
            self._size += 1
            return

        if current is None:
            current = self._first

        if current.next and current.next.data ==  el:
            new_node =  LinkedList.Node(new)
            new_node.next = current.next
            current.next = new_node
            self._size += 1

        if current.next is not None:
            self.recursive_add_before(el, new, current.next)

# Recursive Node Deletion by Value
# Develop a recursive function that removes the first occurrence of a node with a specified value.
# Objective: Implement a function that recursively finds and deletes a node with a given value.
    def recursive_remove_by_value_v2(self, el: object, current=None, previous=None):
        if self._size == 0:
            return None
        
        if current is None:
            current = self._first
                    
        if current.data == el:
            if previous is None:
                self._first = self._first.next
            else:
                previous.next = current.next
            self._size -= 1
            return
        self.recursive_remove_by_value2(el, current.next, current)

    # Recursive Node Deletion by Value: using heper function
    def recursive_remove_by_value(self, el: object):

        def _recursive_remove_helper(current: LinkedList.Node, previous: LinkedList.Node):
            # Checking if the list is empty
            if current is None:
                return None
            # Check if we have found the element
            if current.data == el:
                # If the found element is the first one             
                if previous is None:
                    self._first = self._first.next
                else:
                    previous.next = current.next
                self._size -= 1
                return
            # Recursive call, if we don't find the exact node
            _recursive_remove_helper(current.next, current)
        # Initiating recursing call from the head: the first Node
        _recursive_remove_helper(self._first, None)
                
    
    def reverse(self):
        #!INCOMPLETE
        pass

    
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
                current.next = new_node
                self._size += 1
                break

            current = current.next


    def recursive_add_after(self, el: object, new: object, current=None):
        if self._size == 0:
            return

        if current is None:
            current = self._first

        if current.data == el:
            new_node = LinkedList.Node(new)
            new_node.next = current.next
            current.next = new_node
            self._size += 1
            return
        
        if current.next is None:
            return

        self.recursive_add_after(el, new, current.next)


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
      

#     Implement a recursive remove_at(el: object, index: int) instance method for
# SingleLinkedList class which removes the element at given position. The method should throw a
# ValueError exception in case if the index is out of boundaries. Index valid values are from 0 to size - 1.
# Please note that a static private recursive helper method should be implemented for this task. It receives
# a Node type object to implement the recursion. We define the helper method as static, to operate only
# with nodes inside of it (this method does not have access to list self properties or methods).
    def remove_at(self, index: int):
        if index >= self._size:
            raise ValueError
        
        def _remove_at_helper(current: LinkedList.Node, previous: LinkedList.Node, i=0):
            if current is None:
                return None
            
            if i == index:          
                if previous is None:
                    previous = self._first
                else:
                    previous.next = current.next
                self._size -= 1
                return
            
            _remove_at_helper(current.next, current, i + 1)

        _remove_at_helper(self._first, None)        

    
                
    

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


    class ForwardIterator:
        def __init__(self, start_node):
            self.current_node = start_node

        def __iter__(self):
          return self
        
        def __next__(self):
            if self.current_node is None:
                raise StopIteration
            temp = self.current_node.data
            self.current_node = self.current_node.next
            return temp
        

    # class BackwardIterator:
    #     def __init__(self, last_node):
    #         self.current_node = last_node

    #     def __next__(self):
    #         if self.current_node is None:
    #           raise StopIteration
    #         temp = self.current_node.data
    #         self.current_node = self.current_node.prev
    #         return temp

    #     def __iter__(self):
    #       return self

    class BackIterator:
        def __init__(self, last_node):
            self.current_node = last_node

        def __iter__(self):
            return self
        
        def __next__(self):
          if self.current_node is None:
              raise StopIteration
          temp = self.current_node.data
          self.current_node = self.current_node.prev
          return temp
        

    class SkipIterator:
        def __init__(self, start_node, step: int):
            if step < 1:
                raise ValueError
            self.current_node = start_node
            self.step = step

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current_node is None:
                raise StopIteration
            temp = self.current_node.data
            i = 0
            while i < self.step and self.current_node.next is not None:
                self.current_node = self.current_node.next
                i += 1
            return temp
            
    class CircularIterator:
        def __init__(self, start_node):
            self.current_node = start_node
            self.first_node = start_node

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current_node is None:
                raise StopIteration
            temp = self.current_node.data
            if self.current_node.next is None:
                self.current_node = self.first_node
            else:
                self.current_node = self.current_node.next
            return temp


    def add_first(self, e) -> None:
        new_node = DoubleLinkedList.Node(e)
        if self._size == 0:
            self._first = self._last = new_node
        else:
            new_node.next = self._first
            self._first.prev = new_node
            self._first = new_node
        self._size += 1


    def add_last(self, e: object) -> None:
        new_node = DoubleLinkedList.Node(e)
        if self._size == 0:
            self._first = self._last = new_node
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
    
    def add_after(self, el: object, new: object):
        new_node = DoubleLinkedList.Node(new)
    
        if self._size == 0:
            self._first = self._last = new_node
        else:
            current = self._first
            
            while current:
                if current.data == el:
                    new_node.prev = current
                    new_node.next = current.next
                    
                    if current.next is not None:
                        current.next.prev = new_node
                    else:
                        self._last = new_node
                    
                    current.next = new_node
                    break
                
                current = current.next   
        self._size += 1


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
    
    # O(n) complexity  for
    # finding minimum and maximum elements
    def get_minimum(self): # O(n) complexity
        if self._size == 0:
            return None

        min = self._arr[0]
        for i in range(1, self._size):
            if self._arr[i] < min:
                min = self._arr[i]
        return min

    def get_maximum(self): # O(n) complexity
        if self._size == 0:
            return None

        max = self._arr[0]
        for i in range(1, self._size):
            if max < self._arr[i]:
                max = self._arr[i]
        return max

    def insert_before_max(self, el):
        if self._size == 0:
            self._arr[0] = el
            self._size += 1
            return
        
        max = self._arr[0]
        ind = 0
        for i in range(1, self._size):
            if self._arr[i] > max:
                max, ind = self._arr[i], i
        
        for j in range(self._size, ind, - 1):
            self._arr[j] = self._arr[j - 1]
        self._arr[ind] = el
        self._size += 1

    def reverse(self):
        for i in range(self._size // 2):
            self._arr[i], self._arr[self._size - i - 1] = self._arr[self._size - i - 1], self._arr[i]

    def reverse_rec(self, index=0):
        if self._size == 0:
            return 
        if index >= (self._size // 2):
            return
        self._arr[index], self._arr[self._size - index - 1] = self._arr[self._size - index - 1], self._arr[index]
        self.reverse_rec(index + 1)

            
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
    
#     Implement reorder()->None instance method for ArrayList class which reorders the elements
# [a1, a2, a3, a4, …., an-2, an-1, an] in place to [a1, an, a2, an-1, a3, an-2, …].
    def reorder(self) -> None:
        if self._size <= 1:
            return None
        
        for i in range(1, self._size):
            self.add_at(i, self._arr[self._size - i])

    

    def add_at(self, index, e):
        if index > self._size or index < 0:
            return None
        
        for i in range(self._size - 1, index, -1):
            self._arr[i + 1] = self._arr[i]
        self._arr[index] = e
        self._size += 1

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
    
    def contains(self, el) -> bool:
        if self._size == 0:
            return False
        
        current = self._top
        while current:
            if current.data == el:
                return True
            else:
                current = current.next
        
        return False
    
    #  that removes the first occurrence of a specified element from the stack.
    #  If the element is not found, do nothing.
    def remove(self, el: object):
        if self._size == 0:
            return
        
        previous = None
        current = self._top
        while current:
            if current.data == el:
                if previous is None:
                    self._top = self._top.next
                else:
                    previous.next = current.next
                self._size -= 1
                break

            previous = current
            current = current.next
                

    # that returns the number of times a specified element appears in the stack.
    def count(self, el: object):
        if self._size == 0:
            return 0
        
        count = 0
        current = self._top
        while current:
            if current.data == el:
                count += 1
            current = current.next

        return count
                    
    # that swaps the top two elements of the stack. 
    # If the stack has fewer than two elements, do nothing.
    def swap(self):
        if self._size < 2:
            return
        
        self._top.data, self._top.next.data = self._top.next.data, self._top.data
    
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
            return
        
        self.add_after_recursive(el, new, current.next)

    
    def empty(self) -> None:
        while self._size != 0:
            self.pop()
    
    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size
    
    def display(self):
        if self._size == 0:
            return 
        current = self._top
        while current:
            print(current.data)
            current = current.next
            

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

# Implement a recursive function remove_even_items(s: StackADT) -> int (not within any class
# scope) that removes even items from a stack of integer objects and returns the count of removed items.
# The function should only use the public interface of the Stack (methods like push, pop, and is_empty),
# without accessing private or protected instance properties of the stack object. (
# !def remove_even_items(s: Stack):
#  !   fin_stack = Stack()
#   !  while not s.is_empty():
#    !     if fin_stack[]

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

# Implement a recursive function remove_even_items(s: StackADT) -> int (not within any class
# scope) that removes even items from a stack of integer objects and returns the count of removed items.
# The function should only use the public interface of the Stack (methods like push, pop, and is_empty),
# without accessing private or protected instance properties of the stack object
def remove_even_items(s: Stack) -> int:
    if s.is_empty():
        return "Empty Stack"
    
    t = s.pop()

    count = remove_even_items(s)

    if t % 2 == 0:
        return count + 1
    else: 
        s.push(t)
        return count
    
# Implement a recursive remove_after(s: Stack, el: object) function (not in any class scope)
# which removes the element after the first occurrence of the el. If the stack is empty, raise Exception. If el
# is not in the Stack, raise Exception. If el is the bottom element, raise Exception. Note that no helper
# function should be used to implement the recursion. The function should do the implementation using
# Stack public interface only (you can not access private and protected instance properties of the stack
# object). 
def remove_after(s: Stack, el: object):
    if s.is_empty():
        raise Exception

    t = s.pop()

    if t == el:
        if s.is_empty():
            raise Exception
        else:
            s.pop()
        return
    
    remove_after(s, el)

    s.push(t)

#  Write a recursive function remove_all(s: Stack, el: object) that removes all occurrences
#  of the element el from the stack s. After removing all occurrences, 
# the stack should remain in its original order (except without el).
def remove_all_occurences(s: Stack, el: object):
    if s.is_empty():
        return

    t = s.pop()      

    remove_all_occurences(s, el)

    if t != el:
        s.push(t)

#W rite a recursive function remove_not_divisible(s: Stack, n: int) 
# that removes all elements from the stack that are not divisible by n.
def remove_not_divisible(s: Stack, n: int):
    if s.is_empty():
        return

    t = s.pop()

    remove_not_divisible(s, n)

    if t % n == 0:
        s.push(t)

# Counts the number of elements in the stack `s` that are greater than the specified number `n`.
def count_greater_than(s: Stack, n: int) -> int:
    if s.is_empty():
        return

    t = s.pop()

    count = count_greater_than(s, n)

    if t > n:
        count += 1
    
    s.push(t)

    return count

# Write a recursive function count_even(s: Stack) -> int that returns the count of even elements in the stack.
def count_even(s: Stack) -> int:
    if s.is_empty():
        return 

    t = s.pop()

    count = count_even(s)

    if t % 2 == 0:
        count += 1

    s.push(t)

    return count

# Write a recursive function remove_even(s: Stack) that removes all even elements from the stack.
def remove_even(s: Stack):
    if s.is_empty():
        return

    t = s.pop()

    remove_even(s)

    if t % 2 != 0:
        s.push(t)
