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
    class DivisibleByIterator:
        def __init__(self, num, array, size):
          self.num = num
          self.array = array
          self.size = size
          self.ind = 0

        def __next__(self):
            while self.ind < self.size:         
                if self.array[self.ind] % self.num == 0:
                    temp =  self.array[self.ind]
                    self.ind += 1
                    return temp
                else:
                    self.ind += 1  
            raise StopIteration


    def divisible_by_iterator(self, num: int):
        return ArrayList.DivisibleByIterator(num, self._arr, self._size)

        
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

    @abstractmethod
    def back(self) -> object:
        """Return the back element without removing it."""
        pass

    @abstractmethod
    def swap(v1: object, v2: object) -> None:
        """Swaps the first occurrence of v1 in deque with the first occurrence of v2"""
        pass

   
class Deque(Queue):
    

    def enqueue(self, e: object) -> None:
        """Add an element to the end of the deque."""
        pass

    def dequeue(self) -> object:
        """Remove and return the front element."""
        pass

    def front(self) -> object:
        """Return the front element without removing it."""
        pass

    def back(self) -> object:
        """Return the back element without removing it."""
        pass

    def swap(self, v1: object, v2: object) -> None:
        """Swap the first occurrence of v1 with the first occurrence of v2."""
        pass

    def left_enqueue(self, e: object) -> None:
        """Add an element to the front of the deque."""
        pass

    def right_dequeue(self) -> object:
        """Remove and return the back element."""
        pass

class DoubleLinkedListDeque(Queue):
    class _Node:
        def __init__(self, data, next=None, prev=None):
          self._data = data
          self._next = next
          self._prev = prev
    
    def __init__(self):
      self._first = None
      self._last = None
      self._size = 0

    class StepIterator:
        def __init__(self, start_node : "DoubleLinkedListDeque._Node", step, size):
            if step >= size:
                raise ValueError  
            self.current_node = start_node  
            self.step = step
            self.size = size

        def __iter__(self):
            return self

        def __next__(self):
            temp = self.current_node._data
            i = 0
            while i < self.step:
                if self.current_node is None:
                    raise StopIteration
                self.current_node = self.current_node._next
                i += 1

            return temp

    def left_enqueue(self, e: object):
        new_node = DoubleLinkedListDeque._Node(e)

        if self._size == 0:
            self._first = self._last = new_node
            
        else:
            new_node._next = self._first
            self._first._prev = new_node
            self._first = new_node
        self._size += 1


    def right_dequeue(self):
        if self._size == 0:
            return 

        temp = self._last._data

        if self._size == 1:
            self._first = None
            self._last = None
        else:
            self._last = self._last._prev
            self._last._next = None
            self._size -= 1

        return temp
      
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
        
        temp = self._first._data
        self._first = self._first._next
        self._size -= 1

        if self._size == 0:
            self._last = None

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


class ArrayDeque:
    class StepIterator:
        def __init__(self, step, array, size, start_index):
            if step >= size:
                raise ValueError
            self.step = step
            self.array = array
            self.size = size
            self.current_index = start_index

        def __iter__(self):
            return self

        def __next__(self):
            if self.size == 0:
                raise StopIteration

            temp = self.array[self.current_index]
            self.current_index = (self.step + self.current_index) % self.size
            return temp

    def __init__(self, capacity=10):
        self.size = 0
        self.array = [None] * capacity
        self.front = 0
        self.capacity = capacity

    def step_iterator(self, step):
        self.StepIterator(step, self.capacity, self.size, self.front)

    def dequeue(self) -> object:
        # Checking whether the Deque is empty
        if self.size == 0:
            return

        # Checking whether the Deque contains 1 element
        if self.size == 1:
            temp = self.array[self.front]
            self.array[self.front] = None
            self.front = 0
        else:
            temp = self.array[self.front]
            self.array[self.front] = None
            self.front = (self.front + 1) % self.size

        self.size -= 1
        return temp

    def enqueue(self, e: object):
        self._resize() # Checking if our array is full
    
        if self.size == 0: # Case 1: the array is empty
            self.front = 0
            self.array[self.front] = e
        else:
            new_index = (self.size + self.front) % self.capacity 
            self[new_index] = e

        self.size += 1

    def _resize(self):
        if self.capacity == self.size:
            self.capacity += 10
            new_array = [None] * self.capacity

            for i in range(0, self.size): # Inserting all elements to the newly created array
                new_array[i] = self.array[(self.front + i) % self.size]

            for j in range(self.size):
                self.array[j] = new_array[j]  

            self.front = 0
            

    def duplicate_inplace(self):
        if self.size * 2 > self.capacity: # if no size available for duplication -> resize!
            self._resize()
            
        j = 0
        while j < self.size:
            for i in range(self.size, j, -1): # Shifting elements
                self.array[(i + self.front) % self.capacity] = self[(i - 1 + self.front) % self.capacity]
            # Inserting the duplicate
            self.array[(j + 1 + self.front) % self.capacity] = self.array[(j + self.front) % self.capacity]
            self.size += 1
            j += 2 
        
class SetADT(Collection):
    pass


class MapADT(Collection):
    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def key_set(self) -> SetADT:
        pass

    @abstractmethod
    def values(self) -> List:
        pass  

class HashMap(MapADT):
    class Entry:
        def __init__(self, k, v):
            self._key = k
            self._value = v
            self._next = None

        def get_key(self):
            return self._key
        
        def get_value(self):
            return self._value

    __max_hash = 26

    def __init__(self):
        super().__init__()
        self._hash_table = [None] * self.__max_hash
        self._size = 0

    # make an assumption that we'll store string objects in our set
    def _hash(o: str):
        # Option 1
        # return ord(o[0].lower()) % HashSet.__max_hash
        # Option 2

        return (ord(o[0].lower()) - 97) % HashMap.__max_hash

    def put(self, key, value):
        x = HashMap._hash(key)
        temp = self._hash_table[x]
        if temp is None:
            self._hash_table[x] = HashMap.Entry(key, value)
            self._size += 1
            return value
        while temp:
            if temp._key == key:
                old_value = temp._value
                temp._value = value
                return old_value
            temp = temp._next
        e = HashMap.Entry(key, value)
        e._next = self._hash_table[x]
        self._hash_table = e
        self._size += 1
        return value
   
    def get(self, key):
        x = HashMap._hash(key)
        temp = self._hash_table[x]
        while temp:
            if temp._key == key:
                return temp._value
            temp = temp._next
        return None

    def key_set(self) -> SetADT:
        pass

    def values(self) -> List:
        pass

    def add(self, k) -> None:
        pass

    # def remove(self, k) -> bool:
    #     hash_index = HashMap._hash(k)
    #     curr = self._hash_table[hash_index]
    #     prev = None
    #     while curr:
    #         if curr._key == k:
    #             if not prev:
    #                 self._hash_table[hash_index] = self._hash_table[hash_index]._next
    #             else:
    #                 prev._next = curr._next
    #             self._size -= 1
    #             curr._next = None
    #             return curr._value
    #         prev = curr
    #         curr = curr._next
    #     return None

    def remove(self, k) -> bool:
        x = HashMap._hash(k)
        temp = self._hash_table[x]
        prev = None
        while temp:
            if temp._key == k:
                if prev is None:
                    self._hash_table[x] = self._hash_table[x]._next
                else:
                    prev._next = temp._next
                self._size -= 1
                return True
            prev = temp
            temp = temp._next

        return False

    class HashMapEntryIterator:
        def __init__(self,table):
            self._table=table
            self._current=None
            for i in range(0,len(self._table)):
                if self._table[i] is not None:
                    self._current=self._table[i]
                    break


        def __next__(self):
            x=[self._current.key,self._current.value]
            if self._current._next is not None:
                self._current = self._current._next
            # TODO add the case when the self._current does not have a next reference
            return x

    def __iter__(self):
        return HashMap.HashMapEntryIterator(self._hash_table)

    def contains(self, k) -> bool:
        x = HashMap._hash(k)
        if self._hash_table[x] is None:
            return False
        else:
            return True

    def clear(self) -> None:
        self._hash_table = [None] * HashMap.__max_hash
        self._size = 0

    def print(self):
        for i in range(len(self._hash_table)):
            print(i, ": ", end="")
            temp = self._hash_table[i]
            while temp:
                print("(", temp._key, ",", temp._value, ") ->", end="")
                temp = temp._next
            print()

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

# 2. Create a recursive function, not within any class scope, that accepts a StackADT
# and removes all items at odd | even positions
def stack_even_positions_remover(s: Stack, i=1):
    if s.is_empty():
        return

    t = s.pop()

    stack_even_positions_remover(s, i + 1)

    if i % 2 == 1:
        s.push(t)
    

def stack_odd_positions_remover(s: Stack, i=0):
    if s.is_empty():
        return

    t = s.pop()

    stack_odd_positions_remover(s, i + 1)

    if i % 2 == 0:
        s.push(t)

# 3. Create a recursive function, not within any class scope, that accepts a StackADT
# and removes all items that are divisible by 5.
def remove_divisible_by_5(s: Stack):
    if s.is_empty():
        return

    t = s.pop()

    remove_divisible_by_5(s)

    if t % 5 != 0:
        s.push(t)

# Create a recursive function, not within any class scope, that accepts a StackADT
# and returns the count of all items that are divisible by 5.
def count_of_divisible_by_5_stack(s: Stack):
    if s.is_empty():
        return 0

    t = s.pop()

    count = count_of_divisible_by_5_stack(s)

    if t % 5 == 0:
        count += 1

    s.push(t) 
     
    return count

# Create a recursive function, not within any class scope, that takes a StackADT
# and an object as parameters, and removes the item before that object in the StackADT.
def remove_before_stack(s: Stack, el: object):
    if s.is_empty():
        return

    t = s.pop()

    if s.is_empty():
        s.push(t)
        return
    
    h = s.pop()
    if h == el:
        return
    
    s.push(h)

    remove_before_stack(s, el)

    s.push(t)
        

# Create a recursive function, not within any class scope, that takes StackADT as a
# parameter and returns the maximum object in that stack.
def get_maximum(s: Stack):
    if s.is_empty():
        return float('-inf') # returning very small number

    t = s.pop()

    maximum_item = max(t, get_maximum(s))

    s.push(t)

    return maximum_item

#! Create a recursive function, not within any class scope, that accepts a
#! StackADT and reverses its content. DONE
def reverse_stack(s: Stack):
    if s.is_empty():
        return

    t = s.pop()

    reverse_stack()

    insert_at_bottom(s, t)

def insert_at_bottom(s: Stack, e):
    if s.is_empty():
        s.push(e)
    else:
        t = s.pop()
        insert_at_bottom(s, e)
        s.push(t)
  

# Create a recursive function, not within any class scope, that accepts two
# sorted StackADTs and returns a new merged sorted StackADT (for example, SingleLinkedStack).
def merge_sort_stacks(s1: Stack, s2: Stack) -> Stack:
    if s1.is_empty() and s2.is_empty():
        return

    if s1.is_empty():
        return

    if s2.is_empty():
        return

    t1 = s1.pop()
    t2 = s2.pop()
    result = Stack()

    if t1 > t2:
        result.push(t1)
        result = merge_sort_stacks(s1, s2)
        s2.push(t2)
    else:
        result.push(s2)
        result = merge_sort_stacks(s1, s2)
        s1.push(t1)

    return result


# 1. (Easy) Create a recursive function, not within any class scope, that accepts a
# QueueADT and reverses its content
def reverse_queue(q: Queue):
    if q.is_empty():
        return

    t = q.dequeue()
    
    reverse_queue(q)

    q.enqueue(t)

def remove_odd_positions_queue(q: Queue, i=0):
    if q.is_empty():
        return

    t = q.dequeue()

    remove_odd_positions_queue(q, i + 1)

    if i % 2 == 0:
        q.enqueue(t)

def remove_even_positions_queue(q: Queue, i=1):
    if q.is_empty():
        return

    t = q.dequeue()

    remove_even_positions_queue(q, i + 1)

    if i % 2 == 1:
        q.enqueue(t)

# Create a recursive function, not within any class scope, that accepts a
# QueueADT and removes all items that are divisible by 5
def remove_divisible_by_5_queue(q: Queue):
    if q.is_empty():
        return

    t = q.dequeue()

    remove_divisible_by_5_queue(q)

    if t % 5 != 0:
        q.enqueue(t)

# Create a recursive function, not within any class scope, that accepts a
# QueueADT and returns the count of all items that are divisible by 5.
def count_of_divisible_by_5_queue(q: Queue) -> int:
    if q.is_empty():
        return 0
    
    t = q.dequeue()

    count = count_of_divisible_by_5_queue(q)

    if t % 5 == 0:
        count += 1

    q.enqueue(t)

    return count

#  Create a recursive function, not within any class scope, that takes QueueADT as
# a parameter and returns the minimum object in that queue.
def get_minimum_queue(q: Queue):
    if q.is_empty():
        return
    
    t = q.dequeue()

    minimum_el = min(t, get_minimum_queue(q))

    q.enqueue(t)

    return minimum_el

# Create a recursive function, not within any class scope, that takes a QueueADT
# and an object as parameters, and removes the item before that object in the QueueADT.
def remove_before_queue(q: Queue, el: object):
    if q.is_empty():
        return
    
    t = q.dequeue()

    if q.is_empty():
        q.enqueue(t)
        return
    
    h = q.dequeue()

    remove_before_queue(q, el)

    if h == el:
        return
    else:
        q.enqueue(t)
        q.enqueue(h)

#! Create a recursive function, not within any class scope, that accepts two
#! QueueADTs and removes all items from the first queue that are not present in the
#! second queue.
def intersection_of_queues(q1: Queue, q2: Queue):
    if q1.is_empty or q2.is_empty():
        return

    t = q1.dequeue()

    intersection_of_queues(q1, q2)

    # if t 

#     Implement second_lowest_iterative(q: Queue)-> object and
# second_lowest_recursive(q: Queue)-> object iterative and recursive
# functions not in any class scope which find the second lowest element of the given
# queue.
def second_lowest_iterative(q: Queue)-> object:
    if q.is_empty():
        return None
    
    #! Checking if te queue contains 1 elements

    
    temp_queue = Queue()
    min1 = float('inf')
    min2 = float('inf')

    while not q.is_empty():
        t = q.dequeue()
        temp_queue.enqueue(t)

        if t < min1:
            min2 = min1
            min1 = t
        elif min1 < t < min2:
            min2 = t
        
    while not temp_queue.is_empty():
        q.enqueue(temp_queue.dequeue())
    
    return min2


def second_lowest_recurisve(q: Queue) -> object:
    def _helper_find_min(q) -> object:
        if q.is_empty():
            return float('inf') 
        
        t = q.dequeue()
        
        min_of_rest = _helper_find_min(q)
        
        q.enqueue(t)

        return min(t, min_of_rest)

    def _remove_first_occurrence(q: Queue, target: object):
        if q.is_empty():
            return

        t = q.dequeue()

        if t == target:
            return

        _remove_first_occurrence(q, target)
        q.enqueue(t)

    minimum_el = _helper_find_min(q)

    _remove_first_occurrence(q, minimum_el)

    second_min = _helper_find_min(q)

    return second_min

# Implement merge_sorted_deques_iterative(d1: Deque, d2: Deque) -> Deque
# Impement merge_sorted_deques_recursive(d1: Deque, d2: Deque) -> Deque
#  iterative and recursive functions not in any class scope which return new merged sorted Deque
def merge_sorted_deques_iterative(d1: Deque, d2: Deque)-> Deque:
    if d1.is_empty() and d2.is_empty():
        return None
    
    if d1.is_empty():
        return d2

    if d2.is_empty():
        return d1

    merged = Deque()
    a = d1.dequeue()
    b = d2.dequeue()

    while a is not None and b is not None:
        if a > b:
            merged.enqueue(b)
            b = d2.dequeue()
        else:
            merged.enqueue(a)
            a = d1.dequeue()
    
    while a is not None:
        merged.enqueue(a)
        a = d1.dequeue()

    while b is not None:
        merged.enqueue(b)
        b = d2.dequeue()

    return merged

#!Incomplete???????????
def merged_sorted_deques_recursive(d1: Deque, d2: Deque) -> Deque:
    def add_to_merged(merged: Deque, value):
        merged.enqueue(value)

    if d1.is_empty() and d2.is_empty():
        return Deque()

    if d1.is_empty():
        return d2

    if d2.is_empty():
        return d1

    a = d1.dequeue()
    b = d2.dequeue()

    merged = Deque()

    if a is not None and b is not None:
        if a < b:
            add_to_merged(merged, a)  
            merged = merged_sorted_deques_recursive(d1, d2.enqueue(b)) 
        else:
            add_to_merged(merged, b)            
            merged = merged_sorted_deques_recursive(d1.enqueue(a), d2)  
    elif a is not None:
        
        add_to_merged(merged, a)
        merged = merged_sorted_deques_recursive(d1, d2)

    elif b is not None:
        add_to_merged(merged, b)  
        merged = merged_sorted_deques_recursive(d1, d2)

    return merged
