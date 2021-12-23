#!/usr/bin/python3
import sys
largo = len(sys.argv)
if largo == 1:
    a = 'argument'
else:
    a = 'arguments'
print("{:d} {:s}:".format((largo - 1), a))
for i in range(1, largo):
    print("{:d}: {:s}".format(i, sys.argv[i]))
