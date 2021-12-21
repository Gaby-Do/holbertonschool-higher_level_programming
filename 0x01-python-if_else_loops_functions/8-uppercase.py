#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        i = ord(i)
        if i >= 97 and i < 122:
            print("{:c}".format(i - 32), end='')
        else:
            print("{:c}".format(i), end='')
    print('')
