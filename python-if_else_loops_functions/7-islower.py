#!/usr/bin/python3
def islower(c):  # function that check if c is upper or not
    c = ord(c)  # convert str to ascii value number
    if c > 96 and c < 123:  # if between 'a' & 'z' means lowercase
        return True
    else:
        return False  # means c is uppercase character