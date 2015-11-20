# simple web socket access
# get the data at a specific uri and print to std out

import socket, sys, re

websock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print sys.argv
if len(sys.argv) > 1:
    optionalurl = sys.argv[1]
    urlmatch = re.match(r"(http://.+?/) (.+)", optionalurl)
    print urlmatch
    if (urlmatch):
        website = urlmatch.group(1)
        page = urlmatch.group(2)
        print (website +'/' + page)
    else:
        print "Bad url passed as command line option"
        sys.exit()
else:
    website = "www.py4inf.com"
    page = 'code/romeo.txt'
print website
websock.connect((website, 80))
websock.send('GET http://' + website + '/' + page + ' 1.1 \n\n')

while True:
  data = websock.recv(512)
  if len(data) < 1:
    break
  print data

websock.close()
