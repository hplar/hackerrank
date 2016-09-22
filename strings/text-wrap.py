#!/usr/bin/python3.4

import textwrap
from sys import stdin

print(textwrap.fill(stdin.readline(), int(stdin.readline())))
