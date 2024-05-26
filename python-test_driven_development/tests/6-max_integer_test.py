#!/usr/bin/python3
"""Unittest for max_integer([..])"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        # Ajout d'une vérification pour s'assurer que tous les éléments sont numériques
        if not isinstance(list[i], (int, float)):
            raise TypeError("All list elements must be integers or floats")
        if list[i] > result:
            result = list[i]
        i += 1
    return result
