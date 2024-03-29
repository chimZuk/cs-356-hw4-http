#! /usr/bin/env python
# Dzmitry Kuzmitch

import sys
import socket
import struct
import random
import datetime, time
import os.path

link = sys.argv[1]


#=================== Getting link info and setting connection
link = link.split('/')
host = link[0].split(':')[0]
port = link[0].split(':')[1]
filename = link[1]
server_address = (host, int(port))
#=================== Getting link info and setting connection


#=================== Setting headers
message  = 'GET /' + filename + ' HTTP/1.1\r\n'
message += 'Host: ' + link[0] + '\r\n'

#=================== If cache exists
if os.path.isfile(filename.split('.')[0] + '.cache'):
    secs = os.path.getmtime(filename.split('.')[0] + '.cache')
    tg = time.gmtime(secs)
    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", tg)

    message += 'If-Modified-Since: ' + last_mod_time + '\r\n'
    #=============== If cache exists

message += '\r\n'
#=================== Setting headers


#=================== Trying to connect
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("")
print("")
print("")
print(message)

try:
    sock.connect(server_address)
    sock.sendall(message.encode())
    #=============== Reading data from buffer
    data = b''
    while True:
        buf = sock.recv(1024)
        if not buf:
            break
        data += buf
    sock.close()
    #=============== Reading data from buffer
    data = data.decode()
    headers_array = data.split("\n")

    headers = ""
    for item in headers_array[:6]:
            headers += item
            headers += "\n"

    print(headers)

    content = ""
    if headers_array[0].split(" ")[1] == "200":
        for item in headers_array[6:]:
            content += item
            content += "\n"
        f = open(filename.split('.')[0] + '.cache', "w+")
        f.write(content)
        f.close()

    elif headers_array[0].split(" ")[1] == "304":
        content = ""
        #f = open(filename.split('.')[0] + '.cache', "r")
        #if f.mode == 'r':
            #content = f.read()
            #f.close()

    elif headers_array[0].split(" ")[1] == "404":
        content = "404 Not Found"

    print(content)
    sock.close()
        
except socket.timeout as e:
    print('\nRequest attempt timed out')

except OSError as e:
    print('\nRequest attempt timed out (with an error)')
#=================== Trying to connect
