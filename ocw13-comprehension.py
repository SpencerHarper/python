#!/usr/bin/env python
# ocw13-comprehension.py

string = raw_input('Enter a string: ')
list = []
# create string & list variable to be used later

for x in string:
# make list out of string
	list.append(x)
print list

# ---
# ---

for x in string:
	def parse(x):
		string2 = ''
			if char.isalpha():	
				string2 = string2 + x + '!'
				print string2
			else:
				string2 = string2 + x
				print string2
		return string2	

print parse(string)






