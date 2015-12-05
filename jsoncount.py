# Filename: jsoncount.py
# Author:   Joe Ryan
# Date:     5 December, 2015
# Use:      prompts for a url, reads the json from the url, and sums the comment
#       counts and outputs the answer

import urllib
import json

while True:
    inurl = raw_input("Enter url to retrieve json from: ")
    if len(inurl) < 1 : break

    print 'Retrieving ', inurl, '....'
    url_h = urllib.urlopen(inurl)
    data = url_h.read()
    print 'Retrieved ', len(data), ' characters,'

    info = json.loads(data)
    comment_count = 0
    for comment in info['comments']:
        comment_count += comment['count']

    print "Total comments: ", comment_count
