#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = -number % 10 * -1
else:
    num = number % 10
if num == 0:
    es = "and is 0"
elif num > 5:
    es = "and is greater than 5"
else:
    es = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, num, es))
