# An implementation of the selection sort algorithm.



def find_minimum_with_index(array)
  candidate = array[0]
  candidate_index = 0
  for index in (1...array.length)
    if array[index] < candidate
      candidate = array[index]
      candidate_index = index
    end
  end
  return [candidate, candidate_index]      
end


def selection_sort(array)
  sorted_array = []
  for index in (0...array.length)    
    minimum_index = find_minimum_with_index(array)[1]
    sorted_array.push(array.delete_at(minimum_index))    
  end
  return sorted_array  
end

print selection_sort([9,8,7,6,5,4,3,2,1]).to_s + "\n"


print selection_sort([9,8,6,6,5,100,3,2,1]).to_s + "\n"


