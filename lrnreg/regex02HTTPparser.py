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
        search_for = input("search for the phrase> ")
        resp = requests.get(url)  # Send HTTP GET
        search_me = resp.text      # strip everything off the response as a string (text)

        found=re.findall(search_for, search_me)
        if found:
            print(f"Found {len(found)} match!")
        else:
            print("No match!")

if __name__ == "__main__":
    main()

