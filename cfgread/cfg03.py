#!/usr/bin/env python3

# read filename
filename = input("What is the file to read? ")

## create file object in "r"ead mode
with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
#print(dir(configlist))
linetotal = configlist.count('\n')
print(f"Total lines in file = {linetotal}")

