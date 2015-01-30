class ObjectThatCouldBeInList:
    def __init__(self, value=None):
        self.value = value
        
    def __repr__(self):
        return str(self.value)
        
    def __str__(self):
        return self.__repr__()
        
def objectify(x):
    return ObjectThatCouldBeInList(x)
        

class DoublyLinkedList:

    def __init__(self, *args):
        self.head = None        
        for item in args:
            self.insert(objectify(item))
            
    def search(self, item):
        x = self.head
        while (x is not None) and x.value != item:
            x = x.next
        return x
        
    def insert(self, x):     
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
        
    
        
            