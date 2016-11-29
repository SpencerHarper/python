#!/usr/bin/env python
# ocw19-tuples.py

tuple = (5,6,7,8)

print 'tuple is:', tuple

print 'tuple[2] is:', tuple[2]

for item in tuple:
	print item

(a,b,c,d) = tuple
print 'a is:', a
print 'b is:', b
print 'c is:', c
print 'd is:', d

b = 25

tuple = (a,b,c,d)
print 'tuple is now:', tuple

