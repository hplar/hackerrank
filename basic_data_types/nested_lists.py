#!/usr/bin/python3.4

from sys import stdin
from operator import itemgetter

n = stdin.readline()
students = []
grades = []
worst_students = []

for i in range(int(n)):

    name = stdin.readline().strip("\n")
    grade = float(stdin.readline().strip("\n"))
    grades.append(grade)
    students.append([name, grade])

sorted_students_by_grade = sorted(students, key=itemgetter(1))
second_lowest_grade = sorted(list(set(grades)))[1]

for x, y in sorted_students_by_grade:
    if y == second_lowest_grade:
        worst_students.append(x)

for n in sorted(worst_students):
    print(n)
