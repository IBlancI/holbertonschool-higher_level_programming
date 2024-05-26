#!/usr/bin/env python3
"""
 Class file for ABC class.

"""


from abc import ABC, abstractmethod
""" Define the abstract class Animal"""


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


""" Define the Dog subclass"""


class Dog(Animal):

    def sound(self):
        return "Bark"


""" Define the Cat subclass"""


class Cat(Animal):

    def sound(self):
        return "Meow"
