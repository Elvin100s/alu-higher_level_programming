#!/usr/bin/python3
"""
This script fetches the status from a given URL using the requests library.
"""

import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"  # Correct URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except requests.exceptions.RequestException as e:
        print("Error fetching the URL: {}".format(e))


