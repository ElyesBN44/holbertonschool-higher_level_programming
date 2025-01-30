#!/usr/bin/python3
"""
Module 2-square
Defines a class Square with a private instance attribute size.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square with an optional size.
        
        Args:
            size (int): The size of the square, must be a non-negative integer.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
