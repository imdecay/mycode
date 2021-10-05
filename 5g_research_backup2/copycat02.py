#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import shutil
import os

def main():
   """ Run-time code"""
   # import additional code to complete our task

   os.chdir("/home/student/mycode/")

   shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy2")

   # The following line will create the directory if it does not exist already
   shutil.copytree("5g_research/", "5g_research_backup2/")


# call our main function
main()

