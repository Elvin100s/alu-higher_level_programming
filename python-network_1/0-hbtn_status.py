#!/usr/bin/python3
"""
This script fetches the status from the URL https://alu-intranet.hbtn.io/status
and displays the response body in a formatted manner.
"""

import urllib.request as req

def fetch_status(url):
    """
    Fetches the status from the given URL and prints the response details.

    Args:
        url (str): The URL to fetch the status from.
    """
    with req.urlopen(req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

if __name__ == "__main__":
    fetch_status('https://alu-intranet.hbtn.io/status')
