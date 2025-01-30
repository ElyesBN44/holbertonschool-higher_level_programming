#!/usr/bin/python3
"""Defines a class Square with a private instance attribute 'size'."""


class Square:
    """Represents a square."""
    def __init__(self, size):
        """Initializes the square with a private size."""
        self.__size = size
