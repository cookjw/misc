# Bubble Sort in Ruby
# (sorts a list into ascending order using "bubble sort" algorithm)

def bubble(array)
  for index in (0...array.length - 1)
    if array[index] > array[index + 1]
      greater = array[index]
      lesser = array[index + 1]
      array[index] = lesser
      array[index + 1] = greater
    end  
  end
end

def sorted?(array)  
  for index in (0...array.length - 1)
    if array[index] > array[index + 1]
      return false
    end    
  end
  return true
end

def bubble_sort(array)
  until sorted?(array)
    bubble(array)
  end
  return array  
end


print bubble_sort([9,8,7,6,5,4,3,2,1]).to_s + "\n"


print bubble_sort([9,8,6,6,5,100,3,2,1]).to_s + "\n"