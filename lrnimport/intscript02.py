#!/usr/bin/env python3
import subprocess  ## <-------- changed

subprocess.call(["ip", "link", "show", "up"])

print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")

print(f'\n\n================================')
subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed
print(f'================================')
#subprocess.call(["ip route | grep ens3"]) ## <--- changed

