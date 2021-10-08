#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Solution 01 - JSON to CSV"""

import pandas

def main():

    # create a dataframe from json
    df = pandas.read_excel("movies.xls")

    # writeout dataframe to XML
    df.to_xml("movies-translated-from-excel.xml")

if __name__ == "__main__":
    main()

