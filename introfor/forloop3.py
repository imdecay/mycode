#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting:  farms """

# create a dictionary of farms
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# loop across the dict & list them out
for farmname in farms:
    print(f"\nThe farm name is:  {farmname.get('name')}", end="")   # newline, print current vendor, and end without newline
    print(f"\n   {farmname.get('name')}'s agriculture is:  ", end="")   # newline, print current vendor, and end without newline
    for agitem in farmname.get('agriculture'):
        print(f"{agitem}", end=" ")
    print(f"")


print("\nOur loop has ended.") # print when loop has finished

