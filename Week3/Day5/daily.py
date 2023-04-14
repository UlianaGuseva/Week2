import requests
import time
# before = time.time()
# requests.get("https://www.google.com/")
# after = time.time()
# time = after - before
# print(time)

before = time.time()
requests.get("https://www.youtube.com/")
after = time.time()
time = after - before
print(time)
