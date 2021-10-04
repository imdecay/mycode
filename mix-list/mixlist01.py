#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# print the first item, a string
print("The first item in the list (IP): " + my_list[0] )

# Print the second item, a number, by forcing it into a string
print("The second item in the list (port): " + str(my_list[1]) )

# Print the third item, another string
print("The last item in the list (state): " + my_list[2] )

# Just print the IP addresses
print("These are the two IP addresses:  " + iplist[3] + ", " +  iplist[4])
