#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import shutil
import os

def main():
   """ Run-time code"""
   os.chdir('/home/student/mycode/')
   shutil.move('raynor.obj', 'ceph_storage/')

   # Rename kerrigan
   xname = input('What is the new name for kerrigan.obj? ')
   shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


# call our main function
main()

