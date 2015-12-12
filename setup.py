#!/usr/bin/python
import math
x = input("Insert variable x score ")
y = input("Insert variable y score ")
score = x * y

if x == y:
	print "The number have the same value!"
elif x % y == 0:
	print str(x/y) + "x" +' ' + "= " + str(y/y) + "y" 

# score = x + y
# print score