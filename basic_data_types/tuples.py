#!/usr/bin/python3.4

n = int(input())

# t = split de input op spaties en maak een lijst met integers per character. de lijst wordt daarna omgezet naar tuple
t = tuple([int(n) for n in input().split()])

print(hash(t))
