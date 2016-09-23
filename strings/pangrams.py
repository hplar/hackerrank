#!/usr/bin/python3.4

s = input()
alphabetical_characters = []

for i in s:
    if i.isalpha():
        alphabetical_characters.append(i.lower())

if len(set(alphabetical_characters)) == 26:
    print("pangram")
else:
    print("not pangram")
