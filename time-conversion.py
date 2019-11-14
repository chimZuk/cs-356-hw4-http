#Get current time in UTC/GMT time zone and convert to string in HTTP format:

import datetime, time
tn = datetime.datetime.now(datetime.timezone.utc)
date = tn.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n")
print("Date now: " + date)

#Determining a file’s modification time (in seconds since 1 Jan, 1970 on Unix machines)

import os.path
filename = "filename.html"
secs = os.path.getmtime(filename)


#Convert above time to UTC /GMT (returns a time tuple):

tg = time.gmtime(secs)

 
#Convert above time tuple to a string in HTTP format:

last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", tg)
print("Modified at (HTTP): " + last_mod_time)


#Convert a date/time in string format back to time tuple and seconds since 1 Jan, 1970

tg = time.strptime(last_mod_time, "%a, %d %b %Y %H:%M:%S %Z\r\n")
secs = time.mktime(tg)