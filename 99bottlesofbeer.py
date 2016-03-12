#!/usr/bin/env python

# Author : Shivang Gupta
# Problem Source : http://rosettacode.org/wiki/99_Bottles_of_Beer

for i in range(99,0,-1):
	print(" {number} bottles of beer on the wall \n {number} bottles of beer \n Take one down, pass it around \n {numbernew} bottles of beer on the wall \n\n".format( number = i, numbernew = i-1))

