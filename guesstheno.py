import random
//Command to import the built in python library random

noofguesses=1
no=random.randrange(1,100000)

while noofguesses<16:
	guess=raw_input("Take a guess ")
	guess=int(guess)
	noofguesses=noofguesses+1
	guessesleft=16-noofguesses
	print "Guesses left = ", guessesleft
	if guess<no:
		guessesleft=str(guessesleft)
		print "Your guess is low"
	elif guess>no:
		guessesleft=str(guessesleft)
		print "Your guess is high"
	else:
		noofguesses=str(noofguesses)
		print "Your guess is right"
		exit(0)

print "Game over. You lost. Number = ", no
