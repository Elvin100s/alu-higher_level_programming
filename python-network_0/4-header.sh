#!/bin/bash
# This script sends a GET request to a URL with a custom header.
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
echo "OK"
