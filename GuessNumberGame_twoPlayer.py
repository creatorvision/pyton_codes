#!/usr/bin/env python

import random

var = random.randint(1,1000)
print(" Welcom to Number Guessing Game ")


def checkAnswer(test):
	if var == test:
		print( "You've guessed the correct number")
		return True
	elif var < test:
		print( "Your guess is greater then the number")
		return False
	else :
		print(" Your guess is less than the number ")
		return False

while 1:

	print(" Player One's Chance ")
	test= input('Enter a Integer Number of your wish : ')
	if checkAnswer(test):
		print(" Player One Wins !! Congratulation ")
		break
	else:
		print(" Player Two's Chance :")
		test= input('Enter a Integer Number of your wish : ')
		if checkAnswer (test) :
			print(" Player Two Wins !! Congratulation ")
			break
