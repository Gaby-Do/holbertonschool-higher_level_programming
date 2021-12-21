#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) != 'e':
        if chr(i) != 'q':
            print("{:c}".format(i), end='')
