#!/usr/bin/python3
import sys
if __name__ == "__main__":
    largo = len(sys.argv)
    if largo == 1:
        a = 'arguments.'
    elif largo == 2:
        a = 'argument:'
    else:
        a = 'arguments:'
    largo2 = largo - 1
    print("{:d} {:s}".format(largo2, a))
    for i in range(1, largo):
        print("{:d}: {:s}".format(i, sys.argv[i]))
