#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import json
import crayons

# function to reboot
def devicereboot(iplist): # iplist==list

    for ip in iplist: # looping through the list
        print(f'Connecting to... {ip}') # fstring
        print(f'{crayons.red("REBOOTING NOW!")}')
            # we'll learn to write code that sends cmds to device here
    return None

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    iplist = []
    for ip in devicecmd.keys(): # looping through the dict
        print(f'Handshaking. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'{crayons.red("Attempting to send command -->")} {mycmds}')
            # we'll learn to write code that sends cmds to device here
        iplist.append(ip)

    devicereboot(iplist)
    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    #devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile) # decode the JSON from the file to pythonic data
    print(f'{crayons.green("Data set found")}') # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

# call our main function
main()

