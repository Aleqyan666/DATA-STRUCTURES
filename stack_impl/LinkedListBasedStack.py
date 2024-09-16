class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListBasedStack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node       
        self._size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_node = self.head
        self.head = self.head.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next
