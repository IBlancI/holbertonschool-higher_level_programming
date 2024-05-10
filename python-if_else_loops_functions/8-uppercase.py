#!/usr/bin/python3
def uppercase(str):
    newStr = ""
    for i in str:
        ascii = ord(i)
        if ascii > 96 and ascii < 123:
            ascii = ascii - 32
            newStr = newStr + chr(ascii)
        else:
            newStr = newStr + i
    print("{}".format(newStr))
