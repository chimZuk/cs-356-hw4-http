#! /usr/bin/env python
#Dzmitry Kuzmitch 31479051 Section 101

import sys
import socket
import struct
import random
import time


def connect():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientsocket.settimeout(1)

    question = sys.argv[3] + " A IN"
    questionLength = len(question)
    messageID = random.randint(1,101)

    print("")
    print("Sending Request to " + host + ", " + str(port) + ":")
    print("Message ID: " + str(messageID))
    print("Question Length: " + str(questionLength) + " bytes")
    print("Answer Length: 0 bytes")
    print("Question: " + question)

    packed_data = struct.pack('!hhihh', 1, 0, messageID, questionLength, 0)
    packed_data += bytes(question, 'utf-8')

    for attempt in range(3):

        try:
            clientsocket.sendto(packed_data, (host, port))
            packed_data_echo, address = clientsocket.recvfrom(1024)

            unpacked_data = struct.unpack('!hhihh', packed_data_echo[:12])

            print("")
            print("Received Response from " + host + ", " + str(port) + ":")

            if unpacked_data[4] == 0:
                print("Return Code: " + str(unpacked_data[1]) + " (No errors)")
            else:
                print("Return Code: " + str(unpacked_data[1]) + " (Name does not exist)")

            print("Message ID: " + str(unpacked_data[2]))
            print("Question Length: " + str(unpacked_data[3]) + " bytes")
            print("Answer Length: " + str(unpacked_data[4]) + " bytes")
            print("Question: " + packed_data_echo[12:12 + questionLength].decode("utf-8"))

            if unpacked_data[4] > 0:
                print("Answer: " + packed_data_echo[12 + questionLength:].decode("utf-8"))

            break

        except socket.timeout as e:
            print("")
            print('Request attempt ' + str(attempt + 1) + ' timed out')
            print("Sending Request to " + host + ", " + str(port) + ":")

        except OSError as e:
            print("")
            print('Request attempt ' + str(attempt + 1) + ' timed out (with an error)')
            print("Sending Request to " + host + ", " + str(port) + ":")

def start_request():
    connect()


host = sys.argv[1]
port = int(sys.argv[2])

start_request()
