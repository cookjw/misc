# Merge Sort in Ruby


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