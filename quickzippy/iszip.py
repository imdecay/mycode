#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Using python to create compressed (zipped) archives"""

# standard library imports
import os      # low-level, operating system agnostic commands (i.e. supports most OSes)
import zipfile # tools to create, read, write, append, and list a ZIP file

# function to search for all files within a directory, and add them to our ZIP
def zipdir(dirpath, zipfileobj):
    """does the work of writing data into our zipfile"""
    # os.walk() returns a 3-tuple
    # thats a fancy wany of saying it returns 3 things
    # always in the order... root, dirs, files
    # so the following line says given that you will return to us roots, dirs and files...
    for root, dirs, files in os.walk(dirpath):
        for file in files:  # we only want to loop across the file component
            print(os.path.join(root,file))   # create an aboslute path of where file lives
            zipfileobj.write(os.path.join(root, file)) ## adds files to our zipfileobject that was passed in
    return None # when we are done, no need to return any value


def main():
    """called at runtime"""
    # ask ths user for the directory to be archived
    filename = input("What file are you interested in? ")

    ## If the directory exists, then we can begin archiving it
    if os.path.isfile(filename):
        print("You have a valid file")
        ## zippedfn is the zipped file for the archive
        if zipfile.is_zipfile(filename):
            print(f"{filename} IS a zip file")
        else:
            print(f"{filename} is NOT a zip file")
    else:
        print("Run the script again when you have a valid file to query.")

# this line calls our main function
main()

