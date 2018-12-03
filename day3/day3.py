#!/usr/bin/python3.5
# day3

import sys

# Functions
def functionName(params):
    # do something
    print()

# Main Program
if __name__ == "__main__":
    filename = str(sys.argv[1])
    print("Filename: {}". format(filename))

fileObject  = open(filename, "r")
boxIds = fileObject.read().splitlines()

print(boxIds)

    