#!/usr/bin/python3
# Author - Elvin Cyubahiro

def print_last_digit(number):
    """Function to print the last digit of a number."""
    last_digit = abs(number) % 10
    print("{:02d}".format(last_digit))  # Format to always show two digits
    return last_digit
