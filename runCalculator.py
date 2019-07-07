#!/usr/bin/python3.6
"""
This file is created for usage of a CLI version of the program and creation of an automated
JSON format output. For future use.
"""
from cli_subCal import SubnettingCalculator as subCal
from storage import PermanentStorage as storage
import subprocess
import sys

def main():
    
    if len(sys.argv) != 3:
        print("[-] Usage: python3 runCalculator.py {infile} {outfile}")
        sys.exit(1)
    
    infile = sys.argv[1]
    outfile = sys.argv[2]
        

    dictionary = storage.resultToDict(infile, subCal)
    result = storage.createJSONOutfile(dictionary, outfile, show_output=True)
    print(result)

if __name__ == "__main__":
    main()
