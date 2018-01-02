#!/usr/bin/env python
from math import e

precision = int(input("How many digits of precision:"))

while precision > 50:
    print ("Precision is too large")
    precision = int(input("How many digits of precision:"))
else:
    print (f"{e:.{precision}f")



