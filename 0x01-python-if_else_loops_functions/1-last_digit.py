#!/usr/bin/python3
import random
number = random.radint(-10000, 10000)

if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit > 5:
    print(f"lastdigit of {number:d} is {number:d} lastdigit and is greater than 5")
elif lastdigit < 6 and lastdigit != 0:
    print(f"lastdigit of {number:d} is {number:d} lastdigit and is less than 6 and not 0")
else:
    print(f"lastdigit of {number:d} is 0 and is 0")

