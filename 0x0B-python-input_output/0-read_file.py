#!/usr/bin/python3
"""
0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    opens a file using with, reads and print
    """
    with open(filename, encoding='utf-8') as my_file:
        print(my_file.read(), end='')
