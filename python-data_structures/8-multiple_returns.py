#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = (len(sentence), sentence[:1])
    if sentence:
        return tuple
    else:
        return (0, None)
