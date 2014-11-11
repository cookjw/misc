

def find_minimum_with_index(array)
  candidate = array[0]
  candidate_index = 0
  for index in (1...array.length)
    if array[index] < candidate
      candidate = array[index]
      candidate_index = index
    end
  end
  print "minimum: " + candidate.to_s + "\n"
  return [candidate, candidate_index]      
end

def selection_sort(array)

  # for index in (0...array.length)
    # print "array at step " + (index).to_s + ": " + array.to_s + "\n"
    # element = array[index]
    # minimum = find_minimum_with_index(array[index...array.length])[0]
    # minimum_index = find_minimum_with_index(array[index...array.length])[1]
    # array[index] = minimum
    # array[index...array.length][minimum_index] = element    
    # # array[index...array.length] =  [minimum] + array[index + 1...array.length]
    # print "array after step " + (index + 1).to_s + ": " + array.to_s + "\n"
  # end
  # return array
end


print find_minimum_with_index([9,8,7,6,5,4,3,2,1]).to_s + "\n"


# print selection_sort([9,8,7,6,5,4,3,2,1]).to_s + "\n"