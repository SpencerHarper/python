#!/usr/bin/env python
# ocw-files.py

import pickle

'''
# coply a file to new file
def copyFile(old, new):
	f1 = open(old, 'r')
	f2 = open(new, 'w')
	while True:
		text = f1.read(50)
		if text == '':
			break
		f2.write(text)
	f1.close()
	f2.close()
	return

print '------------------------------'

# using copy function created to copy file to new location & print it
copyFile('test.dat', 'test2.dat')

f2 = open('test.dat', 'r')
text = f2.read()
print text

# create a file, put a string in it
f = open('test.dat', 'w')
f.write('line one\nline two\nline three')
f.close()

# read the file just created
f = open('test.dat', 'r')
print f.read()
f.close()

print '_________________________________'

# creating content for file using variables
title = raw_input('Enter a title: ')
body = raw_input('Enter an entry: ')
journal_entry = 'date\n%s\n%s\n' %(title, body)

# create new file using previously defined variables
f = open('journal_entry.txt','w')
f.write(journal_entry)
f.close()

# defining function that prints dict formated nicely
def report(wages):
	students = wages.keys()
	students.sort()
	for student in students:
		# using variable formatting to make float value line up point in column
		print '%-20s | %10.2f' %(student, wages[student])

#defining dict to be used in function
wages = {'Mary':21.50, 'Joe':23.45, 'John':9.50, 'Dan':4.25}

# using function to format dict nicely
print '_________________________________'
report(wages)
print '_________________________________'


# How to maintain data type when passing non-string
# adding content to new file
f = open('test.pck', 'w')
pickle.dump(12.3, f)
pickle.dump([1,2,3], f)
pickle.dump(15, f)
pickle.dump({1:'this', 2:'test', 3:'worked'}, f)
f.close()

# testing out pickle class load funciton
f = open('test.pck', 'r')
x = pickle.load(f)
print type(x), '\n', x
y = pickle.load(f)
print type(y), '\n', y
z = pickle.load(f)
print type(z), '\n', z
w = pickle.load(f)
print type(w), '\n', w
f.close()

# using exceptions to print custom error reports
name = raw_input('Enter filename: ')
try:
	f = open('name', 'r')
	f.close()
except IOError:
	print 'No file named', name + ', sorry.'

# using function to print custom error reports for multiple types of errors
def exists(filename):
	try:
		f = open(filename)
		f.close()
		return True
	except IOError:
		return 'IOError, oh no!'

# use function created to validate filename
input = raw_input('Enter a filename: ')
print exists(input)
'''

def is_17():
	x = input('Enter a number: ')
	if x == 17:
		raise ValueError, 'That\'s 17, gross.'
	return x

print is_17()


