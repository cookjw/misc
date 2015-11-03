def index_of(mainstr, substr):
    sublength = len(substr)
    for index in range(len(mainstr)):
       if len(mainstr[index:]) >= sublength:
           if equals(substr, mainstr[index: index+sublength]):
               return index
    return -1
    
def equals(str1, str2): 
    if str1 == "":
        if str2 == "":
            return True
        else:
            return False    
    if str1[0] == str2[0]:
        return equals(str1[1:], str2[1:])
    return False
        
    
            
       
       
    