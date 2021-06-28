import time

today = time.strftime('%Y %m %d', time.gmtime()).split()
for x in today:
    print(x)
