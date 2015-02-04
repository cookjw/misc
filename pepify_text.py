from sys import argv
    
    
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

class LinkedList:
    def __init__(self, args):
        self.head = None
        for item in args[::-1]:
            self.insert(item)
            
    def __eq__(self, other):
        current_first = self.head
        current_second = other.head
        if current_first == current_second:
            while current_first and current_second:
                next_first = current_first.next
                next_second = current_second.next
                if current_first == current_second:
                    current_first = next_first
                    current_second = next_second
                else:
                    return False
                    break
            return True
        else:
            return False
        
            
    def __repr__(self):
        return "linked list with head " + str(self.head)
        
    def __str__(self):
        x = self.head
        display = "<--" + str(x) + "-->"        
        while x is not None:
            x = x.next
            display += " " + "<--" + str(x) + "-->"
        return display      
            
    def insert(self, x): 
        x = objectify(x)    
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None
        
    def insert_after(self, existing_node, new_item_value):
        new_node = objectify(new_item_value)
        old_next = existing_node.next
        existing_node.next = new_node
        new_node.next = old_next
        old_next.prev = new_node
        new_node.prev = existing_node
        
    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next            
        else:
            self.head = x.next            
        if x.next is not None:
            x.next.prev = x.prev            

def split(list, node, line, position):
    list.insert_after(node, line[position+1:])
    node.value = line[:position+1] + "\n"    

def find_nearest_space_before(line, position):    
    for index in range(position+1)[::-1]:
        if line[index] == " ":
            return index   

def pepify(list_of_lines, file="pepification_results.txt", maxlength=72):
    linelist = LinkedList(list_of_lines)
    line_node = linelist.head
    while line_node is not None:       
        if len(line_node.value) <= maxlength:
            file.write(str(line_node.value))
        else:
            nearest_space = find_nearest_space_before(line_node.value, maxlength)
            if nearest_space:
                split(linelist, line_node, line_node.value, nearest_space)
                file.write(str(line_node.value))
            else:
                split(linelist, line_node, line_node.value, maxlength)
                file.write(str(line_node.value))
        line_node = line_node.next                

if __name__ == '__main__':
    to_be_pepified = open(argv[1], 'r')
    destination_file = open(argv[2], 'a')
    pepify(to_be_pepified.readlines(), destination_file) 
    destination_file.close()
    to_be_pepified.close()    