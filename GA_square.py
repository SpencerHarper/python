#!/usr/bin/env python

#int1 = raw_input("Enter an int: ")
#int2 = raw_input("Enter an int: ")
#int3 = raw_input("Enter an int: ")
#int4 = raw_input("Enter an int: ")

#int1 = int(int1)
##int2 = int(int2)
#int3 = int(int3)
#int4 = int(int4)

#list = [int1, int2, int3, int4]

#print(list)

#square_list = [(int1*int1), (int2*int2), (int3*int3), (int4*int4)]


my_list = [1,2,3,4,5,6,7]
new_list = list()

for num in my_list:
	num = num**2
	new_list.append(num)


print(new_list)

