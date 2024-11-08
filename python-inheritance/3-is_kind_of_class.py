#!/usr/bin/python3
"""
This module includes a function that determines whether an object is an instance of a specified class or an instance of a class that derives from that specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class.
    """
    return issubclass(type(obj), a_class)
