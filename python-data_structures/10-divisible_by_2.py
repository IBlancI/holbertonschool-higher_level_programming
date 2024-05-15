#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [False] * len(my_list)
    for i in my_list:
        if (i % 2) == 0:
            new_list[my_list.index(i)] = True
    return new_list
