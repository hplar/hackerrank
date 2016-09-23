#!/usr/bin/python3.4

from sys import stdin

n, k = stdin.readline().strip().split()
c = [int(x) for x in stdin.readline().strip().split()]
bc = int(stdin.readline().strip())
ba = int((sum(c) - c[int(k)]) / 2)

if bc == ba:
    print('Bon Appetit')
else:
    print(bc - ba)
