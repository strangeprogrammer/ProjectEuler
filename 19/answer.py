#!/bin/python3

# Key: 0 is Sunday, 1 is Monday, ..., 6 is Saturday
# 0 is January, 1 is February, ..., 11 is December

dayofweek = 1
day = 0
month = 0
year = 1900

total = 0

def getleap():
	global year
	if year % 4:
		return False
	else:
		if year % 100:
			return True
		else:
			if year % 400:
				return False
			else:
				return True

def nextday(monthlen):
	global day, dayofweek, total
	dayofweek = (dayofweek + 1) % 7
	day = (day + 1) % monthlen
	if dayofweek == 0 and day == 0:
		total += 1

def nextmonth():
	global month, day
	if month == 8 or month == 3 or month == 5 or month == 10:
		monthlen = 30
	elif month == 1:
		if getleap():
			monthlen = 29
		else:
			monthlen = 28
	else:
		monthlen = 31
	
	nextday(monthlen)
	while day != 0:
		nextday(monthlen)
	
	month = (month + 1) % 12

def nextyear():
	global year, month
	nextmonth()
	while month != 0:
		nextmonth()
	year += 1

def main():
	global year, total
	while year < 1901:
		nextyear()
	total = 0
	while year < 2001:
		nextyear()
	return total

print(main())
