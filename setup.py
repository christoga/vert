#!/usr/bin/python
import cmath
import setup
import sys
x = input("Insert variable x score ")
y = input("Insert variable y score ")
score = x * y

if x == y:
	print "The number have the same value!"

elif x % y == 0:
	print str(x/y) + "x" +' ' + "= " + str(y/y) + "y" 
    sys.exit()
elif y % x == 0:
	print str(y/x) + "y" +' ' + "= " + str(x/x) + "x" 
    sys.exit()
else:
	print "Something went wrong..."
setup(
    name="Vert",
    version="1.0.0",
    author="Coding Smart School",
    author_email="codingsmartschool@gmail.com",
    url="https://github.com/codingsmartschool/vert",
    description="Find variable's score with vert",
    long_description=("Vert is a python program that takes variable's score"                 
                      " and give user the answer."),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
    ],
    license="MIT",
    packages=['vert'],
)