#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    left_elm = 0
    a_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}

    if roman_string and type(roman_string) is str:
        for i in roman_string[::-1]:
            value = a_dictionary[i]
            if value < left_elm:
                result = result - value
            else:
                result = result + value
                left_elm = value
        return result
    else:
        return 0
