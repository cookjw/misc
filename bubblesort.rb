# Bubble Sort in Ruby
# (sorts a list into ascending order using "bubble sort" algorithm)

def sort()
  puts "Please enter the list (of numbers) you would like to sort. (Elements should be separated by commas, e.g. \"1, 2, 3, 4\".)"
  rawinput = gets.chomp
  inputlist = rawinput.split(",").map { |s| s.to_f } # list elements converted to floats. Don't know how to accept array (instead of string) as user input, like Python input().
    
  def check(list) # checks if list is asscending order; "true" if so, "false" if not
    condition = true 
    for n in (0...list.length - 1)
      if list[n] > list[n+1] then 
        condition = false
        break 
      else
        next              
      end          
    end
    return condition  
  end
  
  def fix(list) # sorts list into ascending order
    for n in (0...list.length - 1)
      if list[n] <= list[n+1] then
        next
      else
        a = list[n]
        b = list[n+1]
        list[n] = b
        list[n+1] = a      
      end    
    end
  end

  while check(inputlist) == false
    fix(inputlist)
  end
  
  puts inputlist
  
end

sort()

