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

    text = text.strip()
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            while text[i + 1] == ' ':
                i += 1
        else:
            print(text[i], end='')
        i += 1
    if i == len(text):
        print()
