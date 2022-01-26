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

    text_update = str(text)
    after_new_line = False
    for c in text_update:
        if after_new_line:
            if c == " ":
                continue
            after_new_line = False
        if c == '.' or c == '?' or c == ':':
            print(c)
            print("")
            after_new_line = True
        else:
            print(c, end="")
