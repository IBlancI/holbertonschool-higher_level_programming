#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_set_1 = set_1 - set_2
    unique_set_2 = set_2 - set_1

    # Combine the unique sets
    result_set = unique_set_1 | unique_set_2

    return result_set