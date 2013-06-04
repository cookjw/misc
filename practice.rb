def pow(a,b)
  if b == 0
    return 1
   
  else
    return a*pow(a, b-1)
  
  end
end
  
A = pow(3,4)

puts A 

def is_prime(num)
  p = false  
    
  if num == 2
    p = true
    
  else
    for i in (2...num)
           
      
      if num % i == 0 
        # puts "found a divisor!"
        p = false      
        break
      else p = true      
      end
      if i = num - 1
          p = true
      end          
    end
    return p
  end
end

def sum(array)
  s = array[0]
  for i in (1..array.size-1)
    s = s + array[i]
  end
  return s
end

list = []

for i in (1..100)
  list << i
end

puts sum(list)



# for i in (1..100)
  # puts i, is_prime(i)
# end 


# def  primes(max)
  # list = Array.new
  # for i in (1..max)
    # if is_prime(i) == true
      # list << i
    # end
  # end
  # return list
  
# end

# puts primes(100)

# def dynamic_constant(n)
  # e = true 
  # if n % 2 == 1
    # e = false  
  # end
  # return e
# end

# for i in (1..100)
  # puts dynamic_constant(i)
# end