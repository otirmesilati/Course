import requests
from time import sleep
time_to_sleep = input("time_to_sleep: ")
sleep(time_to_sleep)

a = int(input("first: "))
b = int(input("second: "))
res = (a/b)
print(res)
