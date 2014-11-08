from sys import stdout
from time import sleep

starting_altitude = int(raw_input("Enter starting altitude.\n"))
# credit: http://stackoverflow.com/a/3249537
digits = len(str(starting_altitude))
delete = "\b" * (digits + 1)
for i in range(starting_altitude + 1):
    sleep(0.5)    
    print "{0}{1:{2}}".format(delete, starting_altitude - i, digits),
print "\n IMPACT"

