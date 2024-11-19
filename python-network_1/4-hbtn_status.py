#!/usr/bin/python3
"""
This script fetches the status from a given URL using the requests library.
"""

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # Updated URL
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


