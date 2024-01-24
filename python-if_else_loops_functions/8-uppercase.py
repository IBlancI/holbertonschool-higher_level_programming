#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            char = chr(ord(str[i]) - 32)
        else:
            char = str[i]
        print("{:s}".format(char), end="")
    print("")