# Project

A simplified version of a HTTP client and server using TCP Sockets. The client program will uses HTTP protocol to fetch a web page (stored in a file) from the server using the HTTP GET method, cache it, and then subsequently uses conditional GET operations to fetch the file only if it has been modified.

# Run

Start server:
```py ./httpserver.py <server IP> <server Port>```

Make a GET request:
```py ./httpclient.py <domain:port/pagename.html>```
