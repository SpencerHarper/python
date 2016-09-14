#!/usr/bin/env python
# ocw02-student_loans.py

# problem statement:

# if you have more than $20,000 in student loans, print something
# if between 0 & 20,000, print something else
# if you have $0 in student loans, print something else

loans=raw_input('Enter total student loans: ')

loans = int(loans)

if loans > 25000:
	print('Wow!')

if loans >= 5000:
	print('That\'s quite a bit.')
else:
	print('Almost gone!')

