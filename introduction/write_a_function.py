#!/usr/bin/python3.4

from sys import stdin

y = int(stdin.readline())


def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    else:
        leap = False
    return leap

print(is_leap(y))
