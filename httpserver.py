#! /usr/bin/env python3
# Dzmitry Kuzmitch 31479051 Section 101

import sys
import socket
import datetime, time
import os.path

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)
contents = ""

count = 0

while True:
    connectionSocket, address = serverSocket.accept()
    data = connectionSocket.recv(10000).decode()
    headers_array = data.split("\n")
    get_header = headers_array[0].split(' ')
    file_name = get_header[1].split('/')[1]

    #=================== Forming headers

    time_now = datetime.datetime.now(datetime.timezone.utc)
    time_now = "Date: " + time_now.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")

    response = ""

    requested_fresh = False

    if os.path.isfile(file_name):
        #============== Getting existing file modification date
        res_time = os.path.getmtime(file_name)
        res_file_time = time.gmtime(res_time)
        last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", res_file_time)
        #============== Getting existing file modification date

        #============== If has modified header
        has_modified_header = False
        modified_header = ""

        for item in headers_array:
            if item.split(" ")[0] == 'If-Modified-Since:':
                has_modified_header = True
                modified_header = item[19:]

        if has_modified_header:
            req_time = time.strptime(modified_header, "%a, %d %b %Y %H:%M:%S %Z\r\n")
            req_file_time = time.mktime(req_time)
            new_res_time = time.mktime(res_file_time)

            if new_res_time > req_file_time:
                response = "HTTP/1.1 200 OK\r\n"
                requested_fresh = False
            else:
                response = "HTTP/1.1 304 Not Modified\r\n"
                requested_fresh = True
        else:
            response = "HTTP/1.1 200 OK\r\n"
            #========== If has modified header
        
        response += time_now

        if requested_fresh == True:
            response += "\r\n"
        else:
            f = open(file_name, "r")
            if f.mode == 'r':
                contents = f.read()
                f.close()

            response += 'Last-Modified: ' + last_mod_time
            response += "Content-Length: " + str(len(contents)) + "\r\n"
            response += "Content-Type: text/html; charset=UTF-8\r\n"
            response += "\r\n"
            response += contents
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += time_now
        response += 'Last-Modified: ' + time_now
        response += "Content-Length: " + str(42) + "\r\n"
        response += "Content-Type: text/html; charset=UTF-8\r\n"
        response += "\r\n"
    #=================== Forming headers
    connectionSocket.send(response.encode())
    connectionSocket.close()