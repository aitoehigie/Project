#!/usr/bin/env python

import math

precision = int(input("How many spaces?"))

while precision > 50:
    print ("The number of spaces is too large")
    precision = int(input("How many spaces?"))
else:
    print ("{math.pi:.{precision}f}")
