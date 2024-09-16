class Node:
    def __init__(self, data=None):
      self.data = data
      self.next = None
      self.prev = None

class LinkedList:
    def __init__(self, head):
     self.head = head

    def append(self, data):
        new_node = Node(data)
        # Check if the list is empty
        if self.head == None:
          self.head = new_node
        else:
           current = self.head
           while current.next:
              current = current.next 
           current.next = new_node
           new_node.prev = current 
    def delete(self, data):
       if self.head == None:
          return 
       
       if self.head.data == data:
          if self.head.next: 
            self.head.next.prev = None
          self.head = self.head.next
          return
       
       current = self.head
       while current:
            if current.data == data:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
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
             current = current.next 

    def display_reverse(self):
       if self.head == None:
        return "empty list"
       else:
          current = self.head
          while current:
             current = current.next
          while current:
             print(current.data)
             current = current.prev
                
    def clear(self):
       if self.head == None:
          return "It's already empty"
       else:
          current = self.head
          while current:
             next_node = current.next
             current.next = None
             current.prev = None
             current = next_node
          self.head = None

    def remove_last(self):
       if self.head == None:
           return "The list is already empty"
       
       if self.head.next == None:
          self.head = None  
          return "Deleted"
       
       current = self.head
       while current.next:
          current = current.next
       current.prev.next = None
       return "Deleted"
    
    def size(self):
       size = 0
       if self.head == None:
         return size
       
       current = self.head
       while current:
          size +=1
          current = current.next
       return size