#!/usr/bin/python3.5
# day4

import sys

# Sort Tuple
# >>> student_tuples = [
#         ('john', 'A', 15),
#         ('jane', 'B', 12),
#         ('dave', 'B', 10),
# ]
# >>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# Main Program
if __name__ == "__main__":
    filename = str(sys.argv[1])
    print("Filename: {}". format(filename))

fileObject  = open(filename, "r")
boxIds = fileObject.read().splitlines()

print(boxIds)

    