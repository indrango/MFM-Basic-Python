import time

localtime   = time.localtime()
timeString  = time.strftime("%Y-%m-%d;%H:%M:%S", localtime)

print timeString
