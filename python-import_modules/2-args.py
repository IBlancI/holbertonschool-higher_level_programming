#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv) - 1
    if args > 1:
        print("{} arguments:".format(args))
        for i in range(1, args + 1):
            print("{}: {}".format(i, argv[i]))
    elif args == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("0 arguments.")