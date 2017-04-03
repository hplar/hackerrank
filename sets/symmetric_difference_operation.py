#!/usr/bin/env python

"""
Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Output total number of students who have subscriptions to the English or the French newspaper but not both.
"""

from sys import stdin

nr_en_subscriptions = int(stdin.readline().strip())
roll_numbers_en = set([x for x in stdin.readline().split()])
nr_fr_subscriptions = int(stdin.readline().strip())
roll_numbers_fr = set([x for x in stdin.readline().split()])

print(len(roll_numbers_en.symmetric_difference(roll_numbers_fr)))
