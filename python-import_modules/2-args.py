#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    args = argv[1:]
    if (len(args) == 0):
        print("0 arguments.")
    elif (len(args) == 1):
        print("1 argument:")
    else:
        print(f"{len(args)} arguments:")
    for i in range(len(args)):
        print(f"{i + 1}: {args[i]}")
