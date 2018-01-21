from random import *

magicNumber=randint(1,10)

usrInput=input("Guess the number between 1 and 10: ")

if int(usrInput) == magicNumber:
	print("You Won! The magic number was {}").format(magicNumber)
else:
	print("Try again! The magic number was {}").format(magicNumber)