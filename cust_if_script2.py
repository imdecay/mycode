#!/usr/bin/env python3
"""Alta3 Research | Dana Kaempen
   ."""

message = "You chose this type of color:"

colors = { 'red': 'warm', 'orange': 'warm', 'yellow': 'warm', 'green': 'middle', 'blue': 'cool', 'black': 'cool' }


# show colors
print(colors.keys())

# ask the user to define "colorchoice"
colorchoice = input("Which color do you want? ")

# doing a lookup on what was chosen in one of the keys... does it match??
# because we want to make a choice of what our response should look like


#### SINGLE LINE SOLUTION
message = f"""{message} {colors.get(colorchoice, "I'm sorry, that color is non-existent")}"""


#### SECOND SOLUTION
#if colorchoice in colors.keys():  # if the color is in the dict
#    message = f"{message} {colors[colorchoice]}"
#else:
#    message = f"{colorchoice} is non-existent"



#### THIRD SOLUTION 
#if colorchoice == 'red' or colorchoice == 'orange' or colorchoice == 'yellow':
#    message = message + 'warm'
#elif colorchoice == 'blue' or colorchoice == 'black':
#    message = message + 'cool'
#elif colorchoice == 'green':
#    message = message + 'middle'
#else:
#    message = message + 'non-existent'

print(message)

