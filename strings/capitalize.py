#!/usr/bin/python3.4

# nope.... doesn't take into account multiple consecutive spaces :-("
# adding a space in last split's argument solves above case

print(' '.join([x.capitalize() for x in input().split(' ')]))
