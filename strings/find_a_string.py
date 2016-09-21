#!/usr/bin/python3.4

from sys import stdin

s = input()
c = input()
matches = []

for i in range(0, len(s)):
    if not s.find(c, i, len(s)) == -1:
        matches.append(s.find(c, i, len(s)))

print(len(set(matches)))