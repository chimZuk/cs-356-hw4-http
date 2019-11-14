#! /usr/bin/env python
#Dzmitry Kuzmitch 31479051 Section 101

import sys
import socket
import struct
import random
import time


def connect():
    print("Sending Request to " + host + ", " + str(port) + ":")
    server_address = (host, port)
    message  = b'GET / HTTP/1.1\r\n'
    message += b'Host: httpbin.org:80\r\n'
    message += b'Connection: close\r\n'
    message += b'\r\n'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(server_address)
        sock.sendall(message)

        data = b''
        while True:
            buf = sock.recv(1024)
            if not buf:
                break
            data += buf

        sock.close()
        print(data.decode())

    except socket.timeout as e:
        print("")
        print('Request attempt timed out')

    except OSError as e:
        print("")
        print('Request attempt timed out (with an error)')


host = sys.argv[1]
port = int(sys.argv[2])

connect()
