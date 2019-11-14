#Get current time in UTC/GMT time zone and convert to string in HTTP format:

import datetime, time
t = datetime.datetime.now(timezone.utc)
date = time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", t)


#Determining a file’s modification time (in seconds since 1 Jan, 1970 on Unix machines)

import os.path
secs = os.path.getmtime(filename)


#Convert above time to UTC /GMT (returns a time tuple):

import time
t = time.gmtime(secs)


#Convert above time tuple to a string in HTTP format:

last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)


#Convert a date/time in string format back to time tuple and seconds since 1 Jan, 1970

t = time.strptime(last_mod_time, "%a, %d %b %Y %H:%M:%S %Z\r\n")
secs = time.mktime(t)