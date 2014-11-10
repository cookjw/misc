def string_reverse(string) # Considerably improved over what used to be here...
  newstring = ""
  for index in (1..string.length)
    newstring = newstring + string[string.length - index]  
  end
  return newstring  
end

puts string_reverse("abcdefghijklmnop")
