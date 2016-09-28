#!/usr/bin/python3.4

from sys import stdin

n = int(stdin.readline().strip())

stomp = '#'
space = ' '

for i in range(n):
    print('{}{}'.format(space*(n-i), stomp*()))