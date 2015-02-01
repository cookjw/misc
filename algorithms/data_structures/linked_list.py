class ObjectThatCouldBeInList:
    def __init__(self, value=None):
        self.value = value
        
    def __repr__(self):
        return str(self.value)
        
    def __str__(self):
        return self.__repr__()
        
    def __eq__(self, other):
        return self.value == other.value
        
def objectify(x):
    return ObjectThatCouldBeInList(x)
        

class DoublyLinkedList:

    def __init__(self, *args):
        self.head = None        
        for item in args:
            self.insert(item)
            
    def search(self, item):
        x = self.head
        while (x is not None) and x.value != item:
            x = x.next
        return x
        
    def insert(self, x): 
        x = objectify(x)    
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None
        
    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next            
        else:
            self.head = x.next            
        if x.next is not None:
            x.next.prev = x.prev
            
            
    def reverse(self):        
        x = self.head
        while (x is not None):            
            next = x.next
            prev = x.prev            
            x.next = prev
            x.prev = next
            if next is None:
                self.head = x            
            x = next

        
    def minimum(self):
        return self.head
        
    def maximum(self):
        x = self.head
        while x.next is not None:
            x = x.next
        return x
        
    def successor(self, x):
        return x.next
        
    def predecessor(self, x):
        return x.prev
        
    

class SinglyLinkedList:

    def __init__(self, *args):
        self.head = None
        for item in args:
            self.insert(item)
            
    def search(self, item):
        x = self.head
        while (x is not None) and x.value != item:
            x = x.next
        return x
        
    def insert(self, x):
        x = objectify(x)
        x.next = self.head
        self.head = x
        
    def delete(self, x):
        y = self.head
        if y == x:
            self.head = x.next            
        while (y is not None) and y.next != x:
            y = y.next
        if y.next == x:
            y.next = x.next            
  
    
    def reverse(self):        
        prev = None # for purposes of pointing item 0's arrow
        x = self.head # starting at item 0        
        while x is not None:            
            next = x.next # saving next item for purposes of advancement
            x.next = prev # reversing current item's arrow         
            prev = x # saving current item for purposes of pointing next item's arrow
            self.head = x # moving the head forward, so that it finally ends up at the last item            
            x = next # moving to next item  
            
    def minimum(self):
        return self.head
        
    def maximum(self):
        x = self.head
        while x.next is not None:
            x = x.next
        return x
        
    def successor(self, x):
        return x.next
        
    def predecessor(self, x):
        y = self.head
        while (y.next is not None) and y.next != x:
            y = y.next
        if y.next == x:
            return y
                    
        
        
        
        

    
            