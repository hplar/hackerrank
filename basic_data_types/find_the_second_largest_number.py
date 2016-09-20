#!/usr/bin/python3.4

"""
break down:
n = single integer input
a = array of integers input, space separated

numbers:    1. take input, split on spaces
            2. convert values to integers (list comprehension)
            3. convert list() to set() to remove matching numbers
            4. convert set() to list() to sort

print(numbers[::-1][1]: 1. print the list, with slicing step on -1 to reverse it
                        2. print the 2nd value (2nd highest number)
                        """

n = input()
a = input()
numbers = sorted(list(set([int(i) for i in a.split()])))
print(numbers[::-1][1])


