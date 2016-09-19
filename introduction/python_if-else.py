#!/usr/bin/python3.4

N = range(1, 100)


def check_weirdness(n):
    # check if odd
    if n % 2 != 0 or n in range(6, 20):
        print("Weird")
    elif n % 2 == 0:
        print("Not Weird")

for i in N:
    check_weirdness(i)
