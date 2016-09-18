#!/usr/bin/env python3

test1,test2,test3 = 'This', 'test', 'worked!'

print('test1: ', test1)
print('test2: ', test2)
print('test3: ', test3)

sentence = '%s is a %s, and it %s!!' %(test1, test2, test3)
print(sentence)
print(sentence[0:14], '!')

list = ['This is', 'a list', 'test.']
tuple = ('This is', 'a tuple', 'test.')
dict = {1:'This is', 2:'a ditionary', 3:'test.'}


print("",list,'\n',tuple,'\n',dict)

del dict[2]
print(dict)


