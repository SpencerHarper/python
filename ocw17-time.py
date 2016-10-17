#!/usr/bin/env python
# ocw17-time.py

class Time:
	def printTime(time):
	       	Time = '%d:%d:%d' %(time.hour, time.minute, time.second)
	        return Time
		pass

time1 = Time()
time1.hour = 9
time1.minute = 25
time1.second = 30

time2 = Time()
time2.hour = 9
time2.minute = 25
time2.second = 29

def isAfter(t1, t2):
	print t1.printTime(), t2.printTime()
	if t1.hour < t2.hour:
		print 't1 < t2'
		return True
	elif t1.hour == t2.hour and t1.minute < t2.minute:
		print 't1.hour == t2.hour and t1.minute < t2.minute'
		return True
	elif t1.hour == t2.hour and t1.minute == t2.minute and t1.second < t2.second:
		't1.hour == t2.hour and t1.minute < t2.minute and t1.second < t2.second'
		return True
	else:
		return False

print isAfter(time1, time2)



