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

    try:
        clientsocket.connect((host , port))
        clientsocket.sendall("GET / HTTP/1.1\r\nHost: www.cnn.com\r\n\r\n")
        print(s.recv(4096))
        clientsocket.close

    except socket.timeout as e:
        print("")
        print('Request attempt timed out')
        print("Sending Request to " + host + ", " + str(port) + ":")

    except OSError as e:
        print("")
        print('Request attempt timed out (with an error)')
        print("Sending Request to " + host + ", " + str(port) + ":")

def start_request():
    connect()


host = sys.argv[1]
port = int(sys.argv[2])

start_request()
