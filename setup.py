#!/usr/bin/python
import cmath
import setup
x = input("Insert variable x score ")
y = input("Insert variable y score ")
score = x * y

if x == y:
	print "The number have the same value!"

elif x % y == 0:
	print str(x/y) + "x" +' ' + "= " + str(y/y) + "y" 
elif y % x == 0:
	print str(y/x) + "y" +' ' + "= " + str(x/x) + "x" 
else:
	print "Something went wrong..."
