#!/usr/bin/python3
"""
4. Text indentation
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
        Arg:
            text(str): text to be printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for char in text:
        if flag == 0:
            if char == '.' or char == ':' or char == '?':
                print(char)
                print()
                flag = 1
            else:
                print(char, end="")
                flag = 0
                continue
        if flag == 1:
            if char == '.' or char == ':' or char == '?' or char == ' ':
                continue    
            else:
                print(char, end="")
                flag = 0
