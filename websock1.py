# simple web socket access
# get the data at a specific uri and print to std out

import socket

websock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
websock.connect(('www.py4inf.com', 80))

websock.send('GET http://www.py4inf.com/code/romeo.txt 1.1 \n\n')

while True:
  data = websock.recv(512)
  if len(data) < 1:
    break
  print data

websock.close()
