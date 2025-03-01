#!/usr/bin/python3

"""add item"""


class Student:
    """
    Defines a student with first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        return {key: value for key, value in self.__dict__.items()
                if isinstance(value, (list, dict, str, int, bool))}
