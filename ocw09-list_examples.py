#!/usr/bin/env python
# ocw08-list_examples.py

list1 = []
string1 = ''


while string1 != 'end':
	string1 = raw_input('Enter a number & \"end\" to quit: ')
	list1.append(string1)

list1.remove('end')
print list1

check = raw_input('do you want to remove an entry (Y/N)?: ')

while check != 'N':
	value = raw_input('enter entry to remove: ')
	list1.remove(value)
	print list1
	check = raw_input('do you want to remove an entry (Y/N)?: ')

check = raw_input('do you want to insert an entry (Y/N)?: ')

while check != 'N':
	value = raw_input('enter position to place entry: ')
	value = int(value)
	value2 = raw_input('what would you like to put there: ')
	list1.insert(value, value2)
	print list1
	check = raw_input('do you want to edit an entry (Y/N)?: ')

print 'that\'s it.'
