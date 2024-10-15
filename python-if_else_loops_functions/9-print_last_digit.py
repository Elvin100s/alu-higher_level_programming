#!/usr/bin/python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)      # Expected output: 8
print_last_digit(0)       # Expected output: 0
r = print_last_digit(-1024) # Expected output: 4
print(r)                  # Expected output: 4
