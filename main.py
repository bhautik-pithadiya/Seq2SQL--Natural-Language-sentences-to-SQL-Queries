from __future__ import unicode_literals, print_function, division
from baseline import baseline
from seq2sql import train as train_target
from seq2sql import test as test_target
import time
from datetime import timedelta

# start = time.time()
# print("Running baseline")
# baseline.run_baseline()
# print('Baseline Time Taken : ', timedelta(seconds=(time.time() - start)))

start1 = time.time()
print("Training target model")
train_target.train_seq2sql()
print("Training Time taken : ", timedelta(seconds=(time.time() - start1)))

start2 = time.time()
print("Testing target model")
test_target.test_seq2sql()
print("Testing Time taken : ", timedelta(seconds=(time.time() - start2)))


print('Total Time Taken : ', timedelta(seconds=(time.time() - start1)))