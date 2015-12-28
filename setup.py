#!/usr/bin/python
import sys

def main():
	x = input("Insert variable x score ")
	y = input("Insert variable y score ")
	score = x * y

	if x == y:
		print "The number have the same value!"

	elif x % y == 0:
		print str(x/y) + "x" +' ' + "= " + str(y/y) + "y" 
	    # sys.exit()
	elif y % x == 0:
		print str(y/x) + "y" +' ' + "= " + str(x/x) + "x" 
	    # sys.exit()
	else:
		print "Something went wrong..."
