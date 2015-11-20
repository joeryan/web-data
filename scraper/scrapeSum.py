# scrapeSum.py
# simple web scraper to scrape numbers from span tags
# practice assignment using BeautifulSoup to extract data from a page
# Joe Ryan
# 11/19/2015

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
summation = 0
tags = soup('span')

for tag in tags:
  summation += int(tag.contents[0])

print summation
