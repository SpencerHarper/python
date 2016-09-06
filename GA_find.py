#!/usr/bin/env python

str = raw_input("Enter a sentence: ")

if str.find("not") < str.find("good"):
	not_index = str.find("not")
	good_index = str.find("good")
	sub_str = str[not_index:(good_index+4)]
#	print(sub_str)
	print(str.replace(sub_str,"bad"))
else:
	print(str)

