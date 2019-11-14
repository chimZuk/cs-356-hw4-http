#! /usr/bin/env python3
# Dzmitry Kuzmitch 31479051 Section 101

import sys
import socket
import struct
import time
import random

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIP, serverPort))

print()
print("The server is ready to receive on port: " + str(serverPort) + "\n")

count = 0

while count < 2:
    packed_data, address = serverSocket.recvfrom(1024)
    print(packed_data)
    serverSocket.sendto("LOL", address)
    count = count + 1
