#!/usr/bin/env python
# ocw18-recursion.py

'''
def rec_sum(list):
	if list == []:
		return 0
	else:
		return list[0] + rec_sum(list[1:])

def fact(n):
	if n < 0:
		return "Error - cannot accept negative numbers."
	elif n == 0:
		return 1
	else:
		return n * fact(n - 1)

list1 = [1,2,3,4]
n = rec_sum(list1)

print fact(n)


def recMult(x, y):
	if x == 1:
		return y
	elif x == 0:
		return 0
	else:
		return y + recMult(x - 1, y)

print recMult(0,5)
print recMult(5,6)
print recMult(6,0)
print recMult(3,4)

def recExp(x,y):
	if y == 0:
		return 1
	else:
		return x * recExp(x, y - 1)

print recExp(1,5)
print recExp(5,2)
print recExp(3,0)
print recExp(0,5)

def recCnt1(n):
	if n == 0:
		return n
	elif n < 0:
		print n
		return recCnt1(n + 1)
	else:
		print n
		return recCnt1(n - 1)

print recCnt1(10)

def recCnt2(x,y):
	if x == y:
		return x
	elif x < 0:
		print y
		return recCnt2(x, y - 1)
	else:
		print y
		return recCnt2(x, y + 1)

print recCnt2(-15,0)

def recStr(input):
	if len(input) == 0:
		return ''
	else:
		return input[-1] + recStr(input[:-1])

print recStr("This is a test.")
'''

def recPri(m):
	def priHelp(m,j):
		if j == 1:
			return True
		else:
			return m % j != 0 and priHelp(m, j - 1)
	return priHelp(m, m - 1)

print recPri(9)
print not recPri(6)



