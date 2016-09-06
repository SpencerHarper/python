#!/usr/bin/env python


def parse(str1,str2):
	str3 = str1[0]+str1[-1]+str2[0]+str2[-1]
	return str3


str1 = raw_input("Enter some text: ")
str2 = raw_input("Enter more text: ")

print(parse(str1,str2))




