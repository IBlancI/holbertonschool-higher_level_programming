#!/usr/bin/python3
""" File class multiples shapes. """
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius ** 2

    def perimeter(self):
        return 2 * pi * abs(self.__radius)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
