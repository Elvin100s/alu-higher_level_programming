#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status and http://0.0.0.0:5050/status
'''

import urllib.request as req

def fetch_status(url):
    with req.urlopen(req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

if __name__ == '__main__':
    # Fetching from the official URL
    fetch_status('https://intranet.hbtn.io/status')
    
    # Fetching from the local server (make sure it's running)
    fetch_status('http://0.0.0.0:5050/status')
