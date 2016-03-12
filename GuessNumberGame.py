#!/usr/bin/env python

import random

var = random.randint(1,100000)
print(" Welcom to Number Guessing Game ")

while 1:

	test= input('Enter a Integer Number of your wish : ')
	if var == test:
		print( "You've guessed the correct number")
		break
	elif var < test:
		print( "Your guess is greater then the number")
	else :
		print(" Your guess is less than the number ")

