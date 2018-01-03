#!/usr/bin/env python

def fibonacci(number):
    seed = [0, 1]
    start = 0
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number >= 2:
        while start <= number:
            seed.append(seed[-1] + seed[-2])
            start += 1
        else:
            return seed


if __name__ == "__main__":
    number = int(input("Enter the number:"))
    print (fibonacci(number))
