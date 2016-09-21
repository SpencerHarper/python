#!/usr/bin/env python
# ocw13-hangman.py

#def max(list1):
#	val_max = None
#	for val in list1:
#		if val > val_max:
#			val_max = val
#	return val_max
#list1 = [12, 15, 32, 7]
#print max(list1)

word = 'claptrap'
# word to be guessed

display = []
# display of game

guessed = []
# letters guessed so far

mistakes = 0
# number of mistakes made

for x in word:
	display.append(x)
print display

input = raw_input('Enter a letter: ')

for x in display:
	if x = input



