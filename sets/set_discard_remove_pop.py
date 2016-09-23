#!/usr/bin/python3.4

from sys import stdin

n = int(stdin.readline().strip())
s = set([int(i) for i in stdin.readline().strip().split()])
N = int(stdin.readline().strip())

for i in range(0, N):
    cmd = stdin.readline().strip()
    if " " in cmd:
        eval("s.{}({})".format(cmd.split()[0], cmd.split()[1]))
    elif " " not in cmd:
        eval("s.{}()".format(cmd))

print(sum(s))
