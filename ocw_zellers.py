#!/usr/bin/env python
# ocw_zellers.py

from string import lower

DAYS = {'0':'Sunday','1':'Monday','2':'Tuesday',\
	'3':'Wednesday','4':'Thursday',\
	'5':'Friday','6':'Saturday'}

MONTHS = {'1':'march','2':'april','3':'may',\
	'4':'june','5':'july','6':'august',\
	'7':'september','8':'october','9':'november',\
	'10':'december','11':'january','12':'february'}

def year_check(MONTH, YEAR):
	if MONTH == 11 or MONTH == 12:
		return YEAR - 1
	else:
		return YEAR

def month_check(MONTH):
	for key, value in MONTHS.iteritems():
		while MONTH == value:
			return int(key) 

def day_check(DAY):
	if DAY < 7:
		R = '0'
		return DAYS[R]
	else:
		R = DAY % 7
		while R < 0:
			R = R + 7
		R = str(R)
		return DAYS[R]

A=raw_input('Enter a  month: ')
B=raw_input('Enter a day of month: ')
X=raw_input('Enter year: ')
C = int(X[-2:])
print 'C:', type(C), C
D = X[0:2]
print 'D:', type(D), D

A = month_check(lower(A))
A = int(A)
B = int(B)
C = int(year_check(A, C))
print 'C after year_check():', type(C), C
D = int(D)

W = (13 * A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2 * D
R = day_check(Z)
print R
