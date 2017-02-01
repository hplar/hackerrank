#!/usr/bin/env python

for i in range(1,int(input())):
    print(int(i * (10**i - 1) / 9))


"""

formula: x * (b**y - 1) / (b - 1)

x = repeated digit
b = used base
y = number of repetitons 

where 0 < x < b


ex.: 5 * (10**4 - 1) / ( 4 - 1 ) = 555
     x     b  y          y

"""
