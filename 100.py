#!/usr/bin/env python

# Author : Shivang Gupta
# Problem Source : http://rosettacode.org/wiki/100_doors

for i in range(1,101):
	
	var = i**0.5
	varint = int(i**0.5)

	if var <= 100 and var==varint:
		print("Door {number} is open".format(number = i))
	else:
		print("Door {number} is closed".format(number = i))





