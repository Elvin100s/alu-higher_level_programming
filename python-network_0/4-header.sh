#!/bin/bash
# Sends request with an added custom header

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send the GET request with the custom header and display the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
