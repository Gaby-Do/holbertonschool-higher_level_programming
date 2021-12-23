#!/usr/bin/python3
import sys
if __name__ == "__main__":
    largo = len(sys.argv)
    sum = 0
    for i in range(1, largo):
        sum = sum + int(sys.argv[i])
    print("{:d}".format(sum))
