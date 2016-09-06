#!/usr/bin/env python

str1 = raw_input("Enter a word: ")
str2 = raw_input("Enter a word: ")
str3 = raw_input("Enter a word: ")
str4 = raw_input("Enter a word: ")

list = [str1, str2, str3, str4]

new_list = list()
for word in list:
	if 'o' in word or 'O' in word:
		new_list.append(word)
print(new_list)

