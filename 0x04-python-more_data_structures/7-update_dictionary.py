#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_d = a_dictionary.copy()
    return(new_d.update({key: value}))
