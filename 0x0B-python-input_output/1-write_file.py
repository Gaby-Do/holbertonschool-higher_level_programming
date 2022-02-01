#!/usr/bin/python3
"""
1. Write to a file
Write a function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, mode='w', encoding='utf-8') as my_file:
        return my_file.write(text)
