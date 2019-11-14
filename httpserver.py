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

    answer = ""
    answerLength = 0
    returnCode = 1

    unpacked_data = struct.unpack('!hhihh', packed_data[:12])
    question = packed_data[12:].decode("utf-8")

    file1 = open("dns-master.txt","r")
    dns_array = file1.readlines()
    file1.close()

    i = 0
    while i < len(dns_array):
        if dns_array[i][0] == '#' or dns_array[i][0] == '\n':
            del(dns_array[i])
        else:
            dns_array[i] = dns_array[i].replace('\n', '')
            i = i + 1

    i = 0
    while i < len(dns_array):
        if question not in dns_array[i]:
            i = i + 1
            continue
        else:
            returnCode = 0
            answer = dns_array[i]
            answerLength = len(answer)
            break
    
    packed_data = struct.pack('!hhihh', 2, returnCode, unpacked_data[2], unpacked_data[3], answerLength)
    packed_data += bytes(question, 'utf-8')

    if returnCode == 0:
        packed_data += bytes(answer, 'utf-8')

    print("Responding to request with message ID " + str(unpacked_data[2]))
    #serverSocket.sendto(packed_data, address)
    count = count + 1
