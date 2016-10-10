#!/usr/bin/env python
# ocw15-assignment3.py

##### Template for Homework 3, exercises 3.1 - ######

from string import *

# **********  Exercise 3.1 ********** 

# Define your function here

def list_intersection(list1, list2):
	list3 = []
	
	for i in list1:
		if i in list2 and i not in list3:
			list3.append(i)
	return list3

# Test Cases for Exercise 3.1

print list_intersection([1, 3, 5], [5, 3, 1])
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
print list_intersection([2, 2, 3, 3], [3, 3, 3, 2, 10])
print list_intersection([2, 4, 6], [1, 3, 5])



# **********  Exercise 3.2 **********

# Define your function here

def ball_collide(ball1, ball2):

	if ball1[0] > ball2[0]:
		dist_x = ball1[0] - ball2[0]
	else:
		dist_x = ball2[0] - ball1[0]
	if ball1[1] > ball2[1]:
		dist_y = ball1[1] - ball2[1]
	else:
		dist_y = ball2[1] - ball1[1]
	if dist_x > dist_y:
		dist = dist_y
	else:
		dist = dist_x
	if (ball1[2] + ball2[2]) > dist: 
		collision = True
	else:
		collision = False
	return collision

# Test Cases for Exercise 3.2

print ball_collide((0, 0, 1), (2, 2, 1)) # Should be False
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True



# **********  Exercise 3.3 **********

# Define your dictionary here - populate with items you've consumed
my_consumption = {'1.0':'coffee', '1.1':'water', '1.2':'tea', '2.0':'quinoa', '2.1':'quorn', '2.2':'chocolate', '3.0':'air', '3.1':'cigarettes', '3.2':'weed'}

def add_item(num, desc):
	number = num
	item = desc
	my_consumption[num] = desc
	return number, item

def print_items(item):
	items = []
	
	for key in my_consumption:
		x = str(key)
		if x[0] == str(item):
			entry = '%s - %s' %(key, my_consumption[key])
			items.append(entry)
	if len(items) == 0:
		return 'No items match this category.'
	else:
		return join(items, '\n')

# Test Cases for Exercise 3.3
print '\nLiquids:\n', print_items(1)
print '\nSolids:\n', print_items(2)
print '\nGases:\n', print_items(3)
print '\nTest:\n', print_items(4)

# Here, use add_consumption to add the item you're going to consume
add_item('1.3', 'juice')
print '\nNew Liquids:\n', print_items(1)



# **********  Exercise 3.4 **********

print '----------------------------'

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
	comb_dict = {}
	count = 0
	while len(l2) > count:
		comb_dict[l1[count]] = l2[count]
		count += 1
	return comb_dict

combined_dict = combine_lists(NAMES, AGES)
#print combined_dict
def people(age):
	age = str(age)
	list = []
#	print 'RUNNING people(age)...'
	for NAME, AGE in combined_dict.iteritems():
		AGE = str(AGE)
#            	print AGE, type(AGE), '||', age, type(age)
#		print NAME, type(NAME)
		if AGE == age:
			list.append(NAME)	
#			print list
	return list

# Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
#print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) == ['Bob']
print people(22) == ['Kelly']
print people(23) == []

print '----------------------------'


# **********  Exercise 3.5 **********

def zellers(month, day, year):
    ##### YOUR CODE HERE #####

    return "Not Yet Implemented"

# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == "Sunday" # This should be True
##### YOUR CODE HERE #####

