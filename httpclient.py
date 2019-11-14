#! /usr/bin/env python
#Dzmitry Kuzmitch 31479051 Section 101

import sys
import socket
import struct
import random
import time


def connect():
    print("Sending Request to " + host + ", " + str(port) + ":")
    request = b"GET / HTTP/1.1\nHost: 127.0.0.1\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        s.send(request)
        result = s.recv(10000)
        print(result)
        clientsocket.close

    except socket.timeout as e:
        print("")
        print('Request attempt timed out')

    except OSError as e:
        print("")
        print('Request attempt timed out (with an error)')

def start_request():
    connect()


host = sys.argv[1]
port = int(sys.argv[2])

start_request()
