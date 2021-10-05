#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   ."""

message = "You chose this type of color:  "
colors = [ 'red', 'orange', 'yellow', 'green', 'blue', 'black' ]

# show colors
print(colors)
colorchoice = input("Which color do you want?  ")

# if input value was higher or equal to 25
if colorchoice == 'red' or colorchoice == 'orange' or colorchoice == 'yellow':
    message = message + 'warm'
elif colorchoice == 'blue' or colorchoice == 'black':
    message = message + 'cool'
elif colorchoice == 'green':
    message = message + 'middle'
else:
    message = message + 'non-existent'
print(message)

