#!/usr/bin/python3
""" print a text """


def text_indentation(text):
    """ print a text """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [".", ":", "?"]
    i = 0
    while i < len(text):
        if text[i] in characters:
            print(text[i], end="")
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end="")
        i += 1
