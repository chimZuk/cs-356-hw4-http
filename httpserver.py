#! /usr/bin/env python3
# TCP Echo Server

import sys
import socket

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
dataLen = 1000000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)

response = "HTTP/1.1 200 OK\r\n"
response += "Date: Sun, 04 Mar 2018 21:24:58 GMT\r\n"
response += "Last-Modified: Fri, 02 Mar 2018 21:06:02 GMT\r\n"
response += "Content-Length: 75\r\n"
response += "Content-Type: text/html; charset=UTF-8\r\n"
response += "\r\n"
response += "<html><p>First Line<br />Second Line<br />Third Line<br />COMPLETE<p><html>"

print(response)

print('The server is ready to receive on port:  ' + str(serverPort) + '\n')

while True:
    connectionSocket, address = serverSocket.accept()
    print("Socket created for client " + address[0] + ", " + str(address[1]))
    data = connectionSocket.recv(dataLen).decode()
    connectionSocket.send(response.encode())

        
