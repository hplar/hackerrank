#!/usr/bin/python3.4

from sys import stdin

m = stdin.readline().strip().split()
set_1 = set([x for x in stdin.readline().strip().split()])
n = stdin.readline().strip().split()
set_2 = set([x for x in stdin.readline().strip().split()])

sym_diff = []

for i in set_1.difference(set_2):
    sym_diff.append(i)
for i in set_2.difference(set_1):
    sym_diff.append(i)

for i in sorted(sym_diff, key=int):
    print(i)
