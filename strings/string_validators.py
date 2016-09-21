#!/usr/bin/python3.4

s = input()

has_alphanum = False
has_alphabet = False
has_digits = False
has_lower = False
has_upper = False

for i in range(0, len(s)):
    if s[i].isalnum():
        has_alphanum = True
    if s[i].isalpha():
        has_alphabet = True
    if s[i].isdigit():
        has_digits = True
    if s[i].islower():
        has_lower = True
    if s[i].isupper():
        has_upper = True

print("{}\n{}\n{}\n{}\n{}".format(has_alphanum, has_alphabet, has_digits, has_lower, has_upper))
