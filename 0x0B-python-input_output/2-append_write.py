#!/usr/bin/python3
"""
2. Append to a file
Write a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends to a file"""
    with open(filename, mode='a', encoding='utf-8') as my_file:
        return my_file.write(text)
