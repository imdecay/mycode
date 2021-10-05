#!/usr/bin/env python3

# request hostname, force to lowercase
hostname = input("What value should we set for hostname?  ").lower()

# if hostname matches, print confirmation
if hostname == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

# announce exit
print("Exiting the script")

