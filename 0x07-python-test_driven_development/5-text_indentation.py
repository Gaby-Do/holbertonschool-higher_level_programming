#!/usr/bin/python3
"""
4. Text indentation
function that prints a text with 2 new lines after each of these characters: ., ? and :
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
    last_i = len(text) - 1
    while i < len(text):
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            if i == last_i:
                break
            if text[1] == ' ' and text[i + 1] == ' ':
                i += 1
        i += 1
