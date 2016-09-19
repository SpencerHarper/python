#!/usr/bin/env python
# ocw07-check_for_vowels.py

def check_vowel(x):
# check if x is a vowel and return true/false
	#x = lower(x)
	# convert x to lowercase to make verifying it easier
	if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
		return True
	else:
		return False

var1 = raw_input('Enter a character: ')
print check_vowel(var1)

def parse_vowel(phrase):
# parse string for vowels
	vowels = ''
	count = 0
	# create a string of vowels
	for x in phrase:
	# if a character in the string is a vowel, do this
		if check_vowel(x):
		# if character in string is vowel, add it to the vowels string
			vowels = vowels + x
			count = count + 1
		# if character in string isn't a vowel, do nothing
	return count, vowels
	print 'test'
	# test showing that nothing after return executes

phrase = raw_input('Enter a string: ')

print parse_vowel(phrase)
