

# merge two lists
# - create new list to hold result of merging
# - start pointer at first element of first list
# - compare first element of first list to first element of second
# - whichever is smaller, put in new list
# - move pointer (if necessary) to element not moved
# - repeat until a list is empty; move the remaining element(s) of the 
# other list (in sorted order) to the new list 

def remove_duplicates(list): # Shouldn't this be built in?
    new_list = []
    for item in list:
        if not item in new_list:
            new_list.append(item)
    return new_list

def merge(list1, list2):
    new_list = []    
    while list1 and list2:  
        smaller = min(list1[0], list2[0])
        new_list.append(smaller)        
        if smaller == list1[0]:
            list1.pop(0)
        elif smaller == list2[0]:
            list2.pop(0)
        else:
            raise Exception("unknown impossible error")
    if list1:
        remainder = list1
    elif list2:
        remainder = list2
    else:
        raise Exception("unknown impossible error")
    new_list += remainder     
    return new_list 

# sort by repeated merging
# - split into lists of length 1
# - if even number, merge each with adjacent; if odd number, merge each
# with adjacent up to penultimate, then merge final 1-element list into
# preceding 2-element list 
# - keep merging adjacent lists until only one list remains; then
# return that list, which should be the sorted result


def merge_sort(list):
    lists = [[item] for item in list]
    while len(lists) > 1:    
        if len(lists) % 2 == 0:
            lists = [merge(lists[index], lists[index+1]) for index in
                        range(0, len(lists) - 1,2)]
        elif len(lists) % 2 == 1:
            prelists = [merge(lists[index], lists[index+1]) for index in 
                        range(0, len(lists) - 2, 2)] 
            lists = prelists[:-1] + [merge(prelists[-1], lists[-1])]
    return lists[0]
            
            
        
        
        
        
        

    
    
    