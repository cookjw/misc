

acceleration = 32.0
terminal_velocity = 183.7
time_to_terminal_velocity = terminal_velocity/acceleration
distance_to_terminal_velocity = 0.5*acceleration*(
    time_to_terminal_velocity
    )**2
def distance_fallen(time)
  if time <= time_to_terminal_velocity
    distance = 0.5*acceleration*(time**2)
  else
   distance = distance_to_terminal_velocity + terminal_velocity*(
            time - time_to_terminal_velocity
            )   
  end
  return distance
end

puts "Enter starting altitude in feet.\n"
starting_altitude = gets.chomp
current_altitude = starting_altitude
start_time = Time.now

while current_altitude > 0
  elapsed_time = Time.now - start_time
  if elapsed_time <= time_to_terminal_velocity
    speed = acceleration*elapsed_time
  else
    speed = terminal_velocity
  end
  current_altitude = starting_altitude - distance_fallen(elapsed_time)
  if current_alititude >= 0
  
  end
end
