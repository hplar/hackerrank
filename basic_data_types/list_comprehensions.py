#!/usr/bin/python3.4

orgList = ["haak", "koe", "vlaak", "tees"]

orgListComp = [x for x in orgList if x.__contains__("a")]
print(orgListComp)
