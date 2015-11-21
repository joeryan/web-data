#!/usr/bin/python

# week2-socks.py
# simple script to retrive a hard coded web page an output to stdout
# used to complete week2 assignment, interpet headers
# writen by Joe Ryan, 8 Nov 2015

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt 1.1\n\n')

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data;

mysock.close()
