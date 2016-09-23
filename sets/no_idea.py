#!/usr/bin/python3.4

n, m = input().strip().split()
array = input().strip().split()
a = set(input().strip().split())
b = set(input().strip().split())

happiness = 0

for i in array:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1

print(happiness)
