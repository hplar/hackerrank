#!/usr/bin/python3.4

from sys import stdin

S = list(stdin.readline())

for i in range(len(S)):
    if S[i].isupper():
        S[i] = S[i].lower()
    elif S[i].islower():
        S[i] = S[i].upper()

print(''.join(S))

