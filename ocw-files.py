#!/usr/bin/env python
# ocw-files.py

import pickle

'''
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
f = open('test.dat', 'w')
f.write('line one\nline two\nline three')
f.close()

f = open('test.dat', 'r')
print f.read()
f.close()

print '------------------------------'

copyFile('test.dat', 'test2.dat')

f2 = open('test.dat', 'r')
text = f2.read()
print text

print '_________________________________'

title = raw_input('Enter a title: ')
body = raw_input('Enter an entry: ')
journal_entry = 'date\n%s\n%s\n' %(title, body)

f = open('journal_entry.txt','w')
f.write(journal_entry)
f.close()

def report(wages):
	students = wages.keys()
	students.sort()
	for student in students:
		print '%-20s | %10.2f' %(student, wages[student])

wages = {'Mary':21.50, 'Joe':23.45, 'John':9.50, 'Dan':4.25}

print '_________________________________'
report(wages)
print '_________________________________'

f = open('test.pck', 'w')
pickle.dump(12.3, f)
pickle.dump([1,2,3], f)
pickle.dump(15, f)
pickle.dump({1:'this', 2:'test', 3:'worked'}, f)
f.close()

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

name = raw_input('Enter filename: ')
try:
	f = open('name', 'r')
	f.close()
except IOError:
	print 'No file named', name + ', sorry.'
'''

def exists(filename):
	try:
		f = open(filename)
		f.close()
		return True
	except IOError:
		return False
	
input = raw_input('Enter a filename: ')
print exists(input)




