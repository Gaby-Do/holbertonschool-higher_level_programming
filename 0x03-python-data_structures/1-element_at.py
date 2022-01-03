#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list):
        return "None"
    elif idx > 0:
        return my_list.pop(idx)
    else:
        return "None"
