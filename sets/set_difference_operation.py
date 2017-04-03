#!/usr/bin/env python

nr_of_english = 9
english_enroll_numbers = set([x for x in "1 2 3 4 5 6 7 8 9".split()])
nr_of_french = 9
french_enroll_numbers = set([x for x in "10 1 2 3 11 21 55 6 8".split()])

print(len(english_enroll_numbers.difference(set(french_enroll_numbers))))
