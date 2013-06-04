def switchindex(n)
  return -n - 1
end

def string_reverse(string)
  length = string.length - 1
  string_init = string[length]
  stringbuilder_list = [string_init]
  string_so_far = string_init
  puts "string_init is %s " % string_init
  puts "string_so_far is %s" % string_so_far
  puts "stringbuilder_list is %s" % stringbuilder_list
  for n in (1...length + 1)
    puts "Now n = %s" % n
	puts "At first, stringbuilder_list is %s" % stringbuilder_list
    stringbuilder_list << string_so_far + string[switchindex(n)]
	puts "Now, stringbuilder_list is %s" % stringbuilder_list
	string_so_far = stringbuilder_list[n]
	puts "And string_so_far is %s" % string_so_far
  end
  if string_so_far == stringbuilder_list[length]
    puts stringbuilder_list[length]
  else
    puts "Sorry, didn't work."
  end
end


string_reverse("abcdefghijklmnop")

#This code seems to work, but the internal steps don't seem to work as I intended. 