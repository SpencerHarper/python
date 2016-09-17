#!/usr/bin/env python
# ocw04-loops.py


string=raw_input('Enter text: ')
count = 0

for letter in string:
	print 'Character number', count, 'is', letter
	count += 1

print 'There were', count, 'characters in the string', string
