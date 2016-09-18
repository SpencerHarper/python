#!/usr/bin/env python
# defining functions in funt.py

def funct(apples, pizzas):
	if apples > 10 and pizzas > 10:
		return True
	else:
		return False

def throw_party():
	count_apples=input('How many apples do you have?: ')
	count_pizzas=input('How many pizzas do you have?: ')

	if funct(count_apples, count_pizzas):
		return 'PARTY!'
	else:
		return 'Need more supplies.'

print funct(20, 20)
print funct(10, 10)
print funct(14, 8)

print throw_party()
