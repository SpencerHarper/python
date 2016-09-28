#!/usr/bin/env python
# ocw15-palindromes.py

from string import *

def flip(string):
	string3 = []
	x = 1
	y = len(string)

	while len(string3) < y:
		string3.append(string[-x])
		x += 1
	return join(string3, '')

def palindrome(string):
	x = len(string) / 2

	string1 = string[:x]
	string2 = string[-x:]
	string3 = flip(string2)
	
	if string1 == string3:
		return 'This is a palindrome!'
	else:
		return 'This is not a palindrome!'

input = raw_input('Enter a string: ')
input = lower(input)
print palindrome(input)

