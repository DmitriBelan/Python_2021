import time

start = time.time()
print(start)
#print(time.asctime())
#print(time.gmtime())
time.sleep(0.0000000000001)
stop = time.time()
print(stop)
print(stop - start)


