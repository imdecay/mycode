#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
the requests library."""

# standard library imports go above 3rd party imports (best practice)
import re

# python3 -m pip install requests
import requests

def main():
    """Search a website's content"""

    url = ''
    while url != 'q':
        print("Where should we search (q to quit)?")
        url = input("> ")  # collect user input
        if url == 'q':
            break
        if url == '':
            print("** Bad input - try again")
            continue
    
        print(f"Great! So we'll try to open this URL {url} to :")
        searchFor = input("search for the phrase> ")
    
        resp = requests.get(url)  # Send HTTP GET
        searchMe = resp.text      # strip everything off the response as a string (text)
    
        # use the re.search() to determine if our website has the pattern we are looking for
        # it works by taking arguments, the first is the regex search pattern, and the second
        # is the string to search within
    
        Found=re.findall(searchFor, searchMe)

        if Found:
            print(f"Found {len(Found)} match!")
        else:
            print("No match!")

if __name__ == "__main__":
    main()

