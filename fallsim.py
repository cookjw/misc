# credit: http://stackoverflow.com/a/3249537


from sys import stdout
from time import time, sleep

starting_altitude = int(raw_input("Enter starting altitude.\n"))
digits = len(str(starting_altitude))
delete = "\b" * (digits + 1)
acceleration = int(raw_input("Enter acceleration. \n"))
# inverse_speed = 1.0/speed # http://lesswrong.com/lw/4z2/inverse_speed/
digits = len(str(starting_altitude))
delete = "\b" * (digits + 1)
current_altitude = starting_altitude
start_time = time()
# while current_altitude > 0:
sleep(0.05)
for i in range(starting_altitude + 1):
    elapsed_time = time() - start_time
    # print i, elapsed_time
    speed = - acceleration * elapsed_time
    # print "speed: " + str(speed)
    inverse_speed = -1.0/speed # http://lesswrong.com/lw/4z2/inverse_speed/
    sleep(inverse_speed)
    print "{0}{1:{2}}".format(delete, starting_altitude - i, digits),
    
    
print "\n IMPACT " + str(elapsed_time)  + " sec."
    


# for i in range(starting_altitude + 1):
    # if speed != 0:
        # inverse_speed = 1.0/speed    
    
    # sleep(inverse_speed)    
    # print "{0}{1:{2}}".format(delete, starting_altitude - i, digits),
# print "\n IMPACT"



