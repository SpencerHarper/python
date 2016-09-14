#!/usr/bin/env python
# ocw03-conditionals.py


input1=raw_input('enter a number: ')
input1 = int(input1)

if input1 > 10:
	print('That\'s greater than 10... good job.')

input2=raw_input('enter another number: ')
input2 = int(input2)

if input2 < 10:
	print('That\'s less than 10. cool.')
else:
	print('That\'s greater than 10. wow.')

input3=raw_input('what\'s your favorite color? ')
input3 = input3.lower()

if input3 == 'green':
	print('good choice.')
elif input3 == 'red':
	print('red can be cool.')
elif input3 == 'blue':
	print('everyone likes blue.')
else:
	print('great.')
