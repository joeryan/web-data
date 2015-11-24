# simple script to take a url from stdin, read XML using urllib, parse using
# ElementTree, and sum up the numbers in count tags
# Joe Ryan, 11/23/2015
# completed as part of UofM class "Using Python to access Web Data" on coursera

import urllib
import xml.etree.ElementTree as ET

dataurl = raw_input("Enter URL of XML to parse for sum of values: ")

urlhandle = urllib.urlopen(dataurl)
xmldata = urlhandle.read()

tree = ET.fromstring(xmldata)
results = tree.findall('.//count')

summation = 0
for result in results:
    summation += int(result.text)

print(summation)
