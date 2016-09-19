#!/usr/bin/env python
# ocw08-string_splice.py

string1 = raw_input('enter a word: ')
# request user enter string to create variable string1 with

print '_____________'

print string1

count = 0
for x in string1:
	if count == 0:
		count = count + 1
	else:
		print x

print '_____________'

print 'indexing with string1[0]:', string1[0]

print 'indexing with string1[0:3]: ' + string1[0:3]

#print type(string1)
# used for testing to ensure type of variable had the len. class

print '_____________'

print 'the length of string is:', len(string1)
print 'the string uppercase is:', string1.upper()
print 'the string lowercase is:', string1.lower()

string2=raw_input('enter a string: ')
string3=raw_input('enter another string: ')

print '_____________'

print 'printed using concatenation:'
print string2 + string3
# no space

print 'printed using comma'
print string2, string3
# added space



