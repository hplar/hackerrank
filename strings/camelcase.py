#!/usr/bin/python3.4

s = input().strip()
w = 0

if s != "":
    w = 1

for i in s:
    if i.isupper():
        w += 1

print(w)
