#!/usr/bin/env python
# Spencer Harper's Split Calculator

def addI(person, item):
	People[person] = People[person] + item
	return

def choose(selection):
	if selection == 'end': 
		person = 'end'
		return person
	else:
	        person = raw_input('Input person: ')
	        if person == 'Mel' or person == 'Dyl'\
		or person == 'Dav' or person == 'Spe'\
		or person == 'Tip':
			newItem = raw_input('Input price of item: $')
		        newItem = float(newItem)
       			People[person] +=  newItem
			return person
		else:
			person = ''
			return person
		
def display(People):
        people = People.keys()
        people.sort()
        for person in People:
		if person != 'Tip':
                	print '%-15s | %10.2f' %(person, People[person])

def tipOut(People, tip):
	people = People.keys()
	for person in People:
		People[person] += tip

x = 0.0
People = {'Tip':x, 'Dyl':x, 'Dav':x, 'Mel':x, 'Spe':x}
selection = ''

while selection != 'end':
	option = raw_input('Enter an action ( \'+\' OR \'end\' ): ')
	if option == 'end':
		selection = 'end'
	elif option == '+':
		if choose(option) == '':
			print 'Choose a valid option.'
			selection = ''
		else:
			selection = ''
	else:
		print 'Choose a valid option.'
		selection = ''

total = 0.0
people = People.keys()
for person in people:
	total += People[person]

tip = People['Tip']

print 'Total: $' + str(total)
print 'Tip: $' + str(tip)
tip = People['Tip'] / 4.0
tipOut(People, tip)
print '-Each: $' + str(tip)
print '-----------------------------------'
display(People)
print '-----------------------------------'
print 'Thanks for using Spencer\'s split calculator.'
print '-----------------------------------'


