#!/usr/bin/env python3

import netifaces

# function to print MAC
def printmac(i): # i==interface
    print('MAC: ', end='')
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
    return None

# function to print IP
def printip(i): # i==interface
    print('IP:  ', end='')
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    return None

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print(f'\n**************Details of Interface - {i} *********************')
    try:
        printmac(i)
        printip(i)
    except:
        print('Could not collect adapter info')


