#!/bin/bash
# This script sends a GET request to a URL with a custom header.

# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request with the specified header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
