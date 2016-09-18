#!/usr/bin/env python
# ocw05_funtions.py
var1 = 10
var2 = 5
def function():
	var1 = 20
	print 'Inside of this function, var1 is:', var1
	return 'Hello world!'
print function()

def funct(var1, var2):
	print 'inside this ideration of the function, var1 is:', var1
	print 'and var2 is:', var2
	return var1**var2
print funct(5, 0)
print funct(5, 3)
print funct(8, 2)

print 'Outside of the function, var1 is:', var1
print 'Outside of the function, var2 is:', var2

