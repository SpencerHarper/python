#!/usr/bin/env python

def addNums(num1, num2):
	sumNums = num1 + num2
	return sumNums

def multiplyNums(num3, num4):
	product = num3*num4
	return product

print("Add the following numbers:")
num1 = raw_input("Enter a number: ")
num2 = raw_input("Enter another number: ")

num1 = int(num1)
num2 = int(num2)

print(addNums(num1,num2))

print("Multiply the following numbers:")
num3 = raw_input("Enter a number: ")
num4 = raw_input("Enter another number: ")

num3 = int(num3)
num4 = int(num4)

print(multiplyNums(num3,num4))

