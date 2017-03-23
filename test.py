__author__ = 'bastanib'

import urllib.request

url = "http://www.google.com"
with urllib.request.urlopen(url) as response:
    html = response.read()

print(html)

