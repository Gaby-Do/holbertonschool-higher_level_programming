#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("value = {:d}".format(value))
        return(True)
    except:
        return(False)
