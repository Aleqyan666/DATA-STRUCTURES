"""This module is designed for collection classes."""
from abc import ABC, abstractmethod
from collections import deque


class Collection(ABC):
    """Collection interface defining a general collection behaviour/type."""

    @abstractmethod
    def empty(self) -> None:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    def print(self) -> None:
        print(self)


class Set(Collection):
    @abstractmethod
    def contains(self, e) -> bool:
        pass

    @abstractmethod
    def add(self, el) -> bool:
        pass

    @abstractmethod
    def remove(self) -> bool:
        pass


class Map(Collection):
    @abstractmethod
    def put(self, k, e) -> object:
        pass

    @abstractmethod
    def get(self, k) -> object:
        pass

    @abstractmethod
    def remove(self) -> object:
        pass

    @abstractmethod
    def value_set(self) -> Set:
        pass

class TreeMap(Map):
    class Entry:
        def __init__(self, k, v, p=None):
            self._right = None
            self._left = None
            self._key = k
            self._value = v
            self._parent = p

    def __init__(self):
        self._root = None
        self._size = 0

    '''
    Task 3: Implement a recursive instance method for TreeMap class which returns a list of keys within the given range.
    The method should throw ValueError in case if the given range is not valid (s > d).
    Note: The recursive helper method should only receive an Entry object (no list) and should return a list. 
    '''
    def get_keys_within_range_postorder(self, s: int, e: int) -> list:
        if s > e:
            raise ValueError
        
        total_keys = self._postorder_recursive_helper(self._root)
        result_keys = []

        for key in total_keys:
            if s <= key <= e:
                result_keys.append(key)

        return result_keys


    def _postorder_recursive_helper(self, entry: "TreeMap.Entry"):
        if entry is None: 
            return []
        
        left_list = self._postorder_recursive_helper(entry._left)
        right_list = self._postorder_recursive_helper(entry._right)

        return left_list + right_list + [entry._key]

    """
    Task 4: Implement a method which returns an iterator for the TreeMap class to iterate over the entries of TreeMap 
    which keys are within the given list and returns the values. 
    """
    class InorderIteratorOnKeys:
        @staticmethod
        def next_inorder(entry: "TreeMap.Entry"):
            if entry is None:
                return None

            p : "TreeMap.Entry" = entry._parent
            if entry._right:
                entry = entry._right
                while entry._left:
                    entry = entry._left
                return entry
            
            while entry._parent:
                p : "TreeMap.Entry" = entry._parent
                if entry == p._left:
                    return p
                entry = p

            return None

        def __init__(self, root, keys):
            self.entry : "TreeMap" = root
            self.keys = keys
            if self.entry:
                while self.entry._left:
                    entry = entry._left

        def __next__(self):
            if self.entry is None:
                raise StopIteration
            
            if self.entry._key not in self.keys:
                self.entry = self.next_inorder(self.entry)
            else: 
                data = self.entry._value
                self.entry = self.next_inorder(self.entry)

            return data
        
        def __iter__(self):
            return self
        
    def inorder_iterator_on_keys(self, keys: list)-> object:
        return self.InorderIteratorOnKeys(self._root, keys) 
        
    class PostorderIteratorOnKeys:
        def __init__(self, root, keys):
            self.entry : "TreeMap.Entry" = root
            self.keys = keys
            if self.entry:
                while self.entry._left or self.entry._right:
                    if self.entry._left:
                        self._entry = self.entry._left
                    else:
                        self.entry = self.entry._right


        @staticmethod
        def next_postorder(entry: 'TreeMap.Entry'):
            if entry is None:
                return None
                
            if entry._parent is None:
                return None
            else:
                p : "TreeMap.Entry" = entry._parent
                if p._right == entry or p._right == None:
                    entry = p
                else:
                    entry = p._right
                    while entry._left or entry._right:
                        if entry._left:
                            entry = entry._left
                        else:
                            entry = entry._right

                return entry

        def __next__(self):
            if self.entry is None:
                return None
            
            if self.entry._key not in self.keys:
                self.entry = self.next_postorder(self.entry)
            else:
                data = self.entry._key
                self.entry = self.next_postorder(self.entry)
            
            return data
                   
        def __iter__(self):
            return self      

    def postorder_iterator_on_keys(self, keys: list) -> object:
        return self.PostorderIteratorOnKeys(self._root, keys)

    class PreorderIteratorOnKeys:
        def __init__(self, root, keys: list):   
            self.entry : "TreeMap.Entry" = root
            self.keys = keys
            
        @staticmethod
        def next_preorder(entry: 'TreeMap.Entry'):
            if entry is None:
                return None
            
            if entry._left:
                return entry._left
                
            if entry._right:
                return entry._right
                
            while entry._parent:
                p : "TreeMap.Entry" = entry._parent
                if entry == p._left and p._right:
                    return p._right
                entry = p

            return None
        

        def __next__(self):
            if self.entry is None:
                raise StopIteration

            while self.entry:
                if self.entry._key not in self.keys: # if the key is not in the list
                    self.entry = self.next_preorder(self.entry) 

                else: # the key was in list, now traverse to next node
                    data = self.entry._value # keep the value
                    self.entry = self.next_preorder(self.entry)
                    return data  
                
            raise StopIteration
             


        def __iter__(self):
            return self

    def preorder_iterator_on_keys(self, keys: list) -> object: 
        return self.PreorderIteratorOnKeys(self._root, keys)