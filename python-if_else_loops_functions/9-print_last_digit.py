#!/usr/bin/python3
# Author - Elvin Cyubahiro


def print_last_digit(number):
    """Function to print the last digit of a number."""
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
