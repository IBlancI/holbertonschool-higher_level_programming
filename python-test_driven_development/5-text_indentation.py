#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """
    Description:
        Function that prints a text with 2 new lines after each of these
        characters: ., ? and :

    Args:
        text = string

    Raises:
        TypeError: If text is not a string

    Returns:
        A new text with the new lines after each of the characters
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        idx = 0
        for i in range(len(text)):
            if i == len(text) - 1:
                print(text[idx:i + 1], end="")
            elif text[i] in [".", "?", ":"]:
                print(text[idx:i + 1] + "\n")
                idx = i + 1
                for j in range(idx, len(text)):
                    if text[j] != " ":
                        idx = j
                        break