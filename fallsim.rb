

Acceleration = 32.0
Terminal_velocity = 183.7
Time_to_terminal_velocity = Terminal_velocity/Acceleration
Distance_to_terminal_velocity = 0.5*Acceleration*(
    Time_to_terminal_velocity
    )**2
def distance_fallen(time)
  if time <= Time_to_terminal_velocity
    distance = 0.5*Acceleration*(time**2)
  else
   distance = Distance_to_terminal_velocity + Terminal_velocity*(
            time - Time_to_terminal_velocity
            )   
  end
  return distance
end

puts "Enter starting altitude in feet.\n"
Starting_altitude = gets.chomp.to_i
$current_altitude = Starting_altitude
Start_time = Time.now

while $current_altitude > 0
  elapsed_time = Time.now - Start_time
  if elapsed_time <= Time_to_terminal_velocity
    speed = Acceleration*elapsed_time
  else
    speed = Terminal_velocity
  end
  $current_altitude = Starting_altitude - distance_fallen(elapsed_time)
  if $current_altitude >= 0
    print "\r", "altitude: ", $current_altitude.round(1), " ft ",
      "speed: ", speed.round(1), " ft/sec ", 
      "time: ", elapsed_time.round(1), " sec"
  end
end

puts "\n 0 \n IMPACT " + elapsed_time.round(1).to_s + " sec" +
  "\n speed: #{speed.round(1)} feet/sec"
