#!/usr/bin/python3.4

from sys import stdin

first_name = stdin.readline().split("\n")[0]
last_name = stdin.readline().split("\n")[0]

print("Hello {} {}! You just delved into python.".format(first_name, last_name))
