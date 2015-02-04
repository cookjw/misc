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
    if isinstance(x, ObjectThatCouldBeInList):
        return x
    else:        
        return ObjectThatCouldBeInList(x)  

class LinkedListSingle:

    def __init__(self, *args):
        self.head = None
        for item in args[::-1]:
            self.insert(item)
           
    def __repr__(self):
        return "linked list with head " + str(self.head)
        
    def __str__(self):
        x = self.head
        display = str(x) + "-->"        
        while x is not None:
            x = x.next
            display += " " + str(x) + "-->"
        return display
        
            
    def search(self, item):
        x = self.head
        while (x is not None) and x.value != item:
            x = x.next
        return x
        
    def insert(self, x):
        x = objectify(x)
        x.next = self.head
        self.head = x        
    
    def insert_after(self, item_in_list, new_item):
        new_item = objectify(new_item)
        new_item.next = item_in_list.next
        item_in_list.next = new_item   
        
    def delete(self, x):
        y = self.head
        if y == x:
            self.head = x.next            
        while (y is not None) and y.next != x:
            y = y.next
        if y.next == x:
            y.next = x.next      



    def reverse(self):
        prev = None
        current = self.head        
        while current is not None:            
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
            

            
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
                    
        
        
class LinkedListDouble:

    def __init__(self, *args):
        self.head = None        
        for item in args[::-1]:
            self.insert(item)
            
    def __repr__(self):
        return "linked list (double) with head " + str(self.head)
        
    def __str__(self):
        x = self.head
        display = "<--" + str(x) + "-->"        
        while x is not None:
            x = x.next
            display += " " + "<--" + str(x) + "-->"
        return display           
    
   
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
        

    
            