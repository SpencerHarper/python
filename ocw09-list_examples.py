#!/usr/bin/env python
# ocw08-list_examples.py

list1 = []
string1 = ''
# create an empty list & string variable to be used later

while string1 != 'end':
# create list of user defined variables
	string1 = raw_input('Enter a number & \"end\" to quit: ')
	list1.append(string1)

list1.remove('end')
print list1
# remove the appended end & display it

check = raw_input('do you want to remove an entry (Y/N)?: ')
while check != 'N':
# see if user wants to remove any items from list
	value = raw_input('enter entry to remove: ')
	list1.remove(value)
	print list1
	check = raw_input('do you want to remove an entry (Y/N)?: ')

check = raw_input('do you want to insert an entry (Y/N)?: ')
while check != 'N':
# see if user wants to add anything to list
	value = raw_input('enter position to place entry: ')
	value = int(value)
	value2 = raw_input('what would you like to put there: ')
	list1.insert(value, value2)
	print list1
	check = raw_input('do you want to edit an entry (Y/N)?: ')

print 'that\'s it.'
