#!/usr/bin/env python
# ocw12-string_operations.py

look = 'Look at me!'
now = ' NOW'

look[:4]
print ' '

look[-1]
print '!'

look*2
print 'Look at me!Look at me!'


look[:-1] + now + look[-1]
print 'Look at me! NOW!'

count = len(now)
for x in now:
	while count > 0:
		count -= 1
		print now[count]

look*2 + look[:-1] + now + look[-1]
print 'Look at me!Look at me!Look at me! NOW!'
