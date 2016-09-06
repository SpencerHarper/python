#!/usr/bin/env python3

import re

x = re.compile('[a-z]+')
#y = re.compile('[]')

input = input('Enter a sentence: ')

output = x.match(input)
#output2 = y.match(input)

print(output)
#print(output2)

