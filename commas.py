def commas(integer):
    number = str(integer)
    length = len(number)
    if length <= 3:
        return number
    else:      
        if length % 3 == 0:
            number_of_groups = length/3
        else:
            number_of_groups = length/3 + 1        
        revnumber = number[::-1]
        revgroups = []
        for i in range(number_of_groups):
            revgroups.append(revnumber[3*i:3*i+3])        
        groupsrev = [group[::-1] for group in revgroups]
        groups = groupsrev[::-1]        
        number = ','.join(groups)
        return number
        

        
print commas(87295)

print commas(123456789)

print commas(123)

print commas(12345678)

print commas(12345678910111213141516171819)
            
            
    
    
    
    