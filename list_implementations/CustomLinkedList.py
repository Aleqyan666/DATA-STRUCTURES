class Node:
    def __init__(self, data=None):
      self.data = data
      self.next = None

class LinkedList:
    def __init__(self):
      self.head = None

    def append(self, data):
        new_node = Node(data)
        # Check if the list is empty
        if self.head == None:
           self.head = new_node
        # Start from the head of the list & traverse the list until reaching the last node
        else:
          current = self.head
          while current.next:
             current = current.next
          current.next = new_node # Point the last node to the new node 

    def delete(self, data):
        if self.head == None:
           return 
        
        if self.head.data == data:
           self.head = self.head.next
           return 
        
        current = self.head
        while current.next:
           if current.next.data == data:
              current.next = current.next.next
              return
           current = current.next

    def find(self, data):
         current = self.head
         while current:
            if current.data == data:
               return current
            current = current.next
         return None

    def display(self):
       if self.head == None:
          return "empty list"
       else:
          current = self.head
          while current:
             print(current.data)
    
    def clear(self):
       if self.head == None:
          return "It's already empty"
       else:
          current = self.head # Marking the first element
          while current: # Iterating over all elements
             next_node = current.next
             current.next = None
             current = next_node
          
          self.head = None

    def remove_last(self):
       if self.head == None:
          return "The list already empty"
       
       if self.head.next == None:
          self.head = None
          return "Deleted !"
       
       current = self.head
       while current.next and current.next.next:# Checking that the current is not նախավերջին
          current = current.next
       current.next = None
       return "Deleted !"  
    
    def size(self):
       size = 0
       if self.head == None:
         return size
       
       current = self.head
       while current:
          size +=1
          current = current.next
       return size