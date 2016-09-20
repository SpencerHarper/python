#!/usr/bin/env python
# ocw11-list_operations.py

import math
# import python module named math
#	it provides use of mathematical functions

list1 = [3, 5, 6, 12]
# 3
print list1[0]

# [5, 6, 12]
print list1[1:]

# 3
# 5
# 6
# 12
for x in list1:
	print x

# [12, 6, 5, 3]
list2 = []
for x in list1:
	list2.insert(0, x)
print list2

# [9, 15, 18, 36]
list2 = []
for x in list1:
	list2.append(x * 3)
print list2

# [False, False, True, True]
def check(x):
	if x > 5:
		return True
	else:
		return False
list2 = []
for x in list1:
	list2.append(check(x))
print list2

