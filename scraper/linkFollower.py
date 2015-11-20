# linkFollower.py
# follows links at a specific position a specific number of times
# part of the assignments for University of Michigan course:
# Using Python to Access Web Data - offered on Coursera.org
# Author: Joe Ryan
# 19 November, 2015

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')

for i in range(0, int(count)):
    print 'Retrieving ' + url + '.....'
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[int(position)].get('href', None)

print 'Last URL: ', url
