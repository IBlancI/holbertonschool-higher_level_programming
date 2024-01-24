#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit_str = "-" + str(lastdigit)
else:
    lastdigit_str = lastdigit

lastdigit_int = int(lastdigit_str)

if lastdigit_int > 5:
    str = "and is greater than 5"
elif lastdigit_int < 6 and lastdigit_int != 0:
    str = "and is less than 6 and not 0"
else:
    str = "and is 0"

print(f"Last digit of {number} is {lastdigit_str} {str}")