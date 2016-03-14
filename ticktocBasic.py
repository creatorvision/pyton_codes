#!/usr/bin/python

# Author : Shivang Gupta
# A simple program to play two player Tic- Tac.

import sys, traceback

print(" 3x3 TIC TAC Games Begin")
print("\n\n please in your turn provide input in the format of \"x,y\" and name also in the format \"your-name\"")

try:
	player1 = input("Player1 input your name: ")
	player2 = input("player2 input your name: ")
except Exception:
	print("ERROR")
	if(isinstance(player1,basestring) or isinstance(player2,basestring)):
		print("You have entered a non string value")
		sys.exit(0) 
	sys.exit(0)

win= False
l=[[0,0,0],[0,0,0],[0,0,0]]
def checkWin(x,y,playerid):
		l[x][y]=playerid
		draw(x,y)
		if check(playerid):
			return True

def check(playerid):

	# Checking Horizontal match
	for i in range(0,3):
		if(l[i][0]==playerid and l[i][1]==playerid and l[i][2]==playerid):
			return True
	# Checking Vertical match
	for i in range(0,3):
		if(l[0][i]==playerid and l[1][i]==playerid and l[2][i]==playerid):
			return True
	# Checking cross match
	if(l[0][0]==playerid and l[1][1]==playerid and l[2][2]==playerid):
		return True
	elif(l[2][0]==playerid and l[1][1]==playerid and l[0][2]==playerid):
		return True
	else :
		return False

def draw(x,y):
	for i in range(0,3):
			print 	'[',l[i][0], ']', ' [', l[i][1], '] ' ,'[' , l[i][2], '] '


while win==False :

	str1=input( player1+ " Your Turn : \n (Choose the x,y coordinates where you want to play your turn)")
	player1x=int(str1[0])
	player1y=int(str1[2])
	#draw(player1x,player1y)
	if checkWin(player1x,player1y,1):
		win=True
		print(player1+ "Wins !")
		break
	else:
		str2=input(player2+ " Your Turn : \n (Choose the x,y coordinates where you want to play your turn)")
		player2x=int(str2[0])
		player2y=int(str2[2])
		#draw(player2x,player2y)
		if checkWin(player2x,player2y,2):
			win=True
			print(player2+"Wins !")
			break
		else:
			continue

print("GAME OVER")
