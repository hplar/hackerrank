#!/usr/bin/python3.4

from sys import stdin

n = int(stdin.readline().strip())
s = set('')

for _ in range(n):
    s.add(stdin.readline().strip())

print(len(s))
