#!/usr/bin/env python

#str1 = raw_input("Enter a word: ")
#str2 = raw_input("Enter a word: ")
#str3 = raw_input("Enter a word: ")
#str4 = raw_input("Enter a word: ")

#list = (str1, str2, str3, str4)



my_list = [20,14,14,14,10,10,20]
new_list = list()
for item in my_list:
	if item not in new_list:
		new_list.append(item)
print(new_list)




