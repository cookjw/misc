# Merge Sort in Ruby

# merge two lists
# - create new list to hold result of merging
# - start pointer at first element of first list
# - compare first element of first list to first element of second
# - whichever is smaller, put in new list
# - move pointer (if necessary) to element not moved
# - repeat until a list is empty; move the remaining element(s) of the 
# other list (in sorted order) to the new list 


def merge(array1, array2)
  new_array = []
  until array1.empty? or array2.empty?
    smaller = [array1[0], array2[0]].min
    new_array.push(smaller)
    if smaller == array1[0]
      array1.shift
    elsif smaller == array2[0]
      array2.shift 
    else
      raise StandardError, "unknown impossible error"    
    end    
  end
  
  if array2.empty?
    remainder = array1    
  elsif array1.empty?
    remainder = array2    
  else
    raise StandardError, "unknown impossible error"   
  end
  
  new_array += remainder
  return new_array

end

# sort by repeated merging
# - split into lists of length 1
# - if even number, merge each with adjacent; if odd number, merge each
# with adjacent up to penultimate, then merge final 1-element list into
# preceding 2-element list 
# - keep merging adjacent lists until only one list remains; then
# return that list, which should be the sorted result

def merge_sort(array)
  arrays = array.map{|item| [item]}
  while arrays.length > 1
    if arrays.length % 2 == 0
      arrays = (0...arrays.length - 1).step(2).map do
        |index| merge(arrays[index], arrays[index+1])
      end
    elsif arrays.length % 2 == 1
      prearrays = (0...arrays.length - 2).step(2).map do
        |index| merge(arrays[index], arrays[index+1])
      end
      arrays = prearrays[0...-1] + [merge(prearrays[-1], arrays[-1])]     
    end
  end
  
  return arrays[0]

end