import time
from datetime import timedelta


start = time.time()

time.sleep(5)
time_taken = 120#time.time() - start

print('%d' % (time_taken/60))