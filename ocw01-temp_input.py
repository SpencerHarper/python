#!/usr/bin/env python
#temp example

city=raw_input("Enter a city: ")
while city [-1]==" ":
	city = city[:-1]
temp=raw_input("Enter a temperature in F: ")
temp = float(temp)
temp = (temp - 32.0)*(100.0/180.0)
temp = round(temp,3)
temp = str(temp)
print('In ' + city + ' it is ' + temp + ' degrees Celcius.')
