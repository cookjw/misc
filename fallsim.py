from time import time

acceleration = 32.0
terminal_velocity = 183.7
time_to_terminal_velocity = terminal_velocity/acceleration
distance_to_terminal_velocity = 0.5*acceleration*(
    time_to_terminal_velocity
    )**2
def distance_fallen(time):
    if time <= time_to_terminal_velocity:
        distance = 0.5*acceleration*(time**2)
    else:         
        distance = distance_to_terminal_velocity + terminal_velocity*(
            time - time_to_terminal_velocity
            )   
    return distance    

starting_altitude = int(raw_input("Enter starting altitude in feet.\n"))
current_altitude = starting_altitude
start_time = time()
while current_altitude > 0:
    elapsed_time = time() - start_time
    if elapsed_time <= time_to_terminal_velocity:
        speed = acceleration*elapsed_time
    else:
        speed = terminal_velocity
    current_altitude = starting_altitude - distance_fallen(elapsed_time) 
    if current_altitude >= 0:    
        print "\r", "altitude:", round(current_altitude, 1), "ft ", \
            "speed:", round(speed, 1), "ft/sec ", \
            "time:", round(elapsed_time, 1), "sec", 
    
print "\n 0 \n IMPACT " + str(round(elapsed_time, 1))  + " sec" + \
    "\n speed: {0} feet/sec".format(round(speed, 1))

    



