#!/usr/bin/python3.4

from sys import stdin

S = stdin.readline()
i, c = stdin.readline().split()

print("{}{}{}".format(S[:int(i)], c, S[int(i)+1:]))
