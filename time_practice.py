import threading, time


start = time.time()

threadObj = threading.Thread(target=time.sleep, args=[5])
threadObj.start()
time.sleep(5)

end = time.time()

time_period = end - start
print(time_period)
