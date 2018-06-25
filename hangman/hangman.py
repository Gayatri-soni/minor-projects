import datetime
import time


def inp():
	print("you wanna try again ?enter y or Y  and to exit press any key..")      #asking player to play again.
	x=input()
	if x=="y" or x=="Y":
		nam()                   #if condition satisfied then name is asked again to start new game..
	else:
		print("Thanks for playing.. see you again!!")         #in case player wants to exit..
		exit()
		
def exit():                               #exit function to quit the game..
	print("Have a gud day !")
		
def hang():                               #this function includes actual game to be played
	print ("Start guessing...")
	time.sleep(0.5)

	#here we set the secret
	word = "krishna"

	#creates an variable with an empty value
	guesses = ''

	#determine the number of turns
	turns = 10

	# Create a while loop

	#check if the turns are more than zero
	while turns > 0:         

		# make a counter that starts with zero
		fail = 0             

		# for every character in secret_word    
		for char in word:      

		# see if the character is in the players guess
			if char in guesses:    
		
			# print then out the character
				print (char)    

			else:
		
			# if not found, print a dash
				print ("_")     
		   
			# and increase the failed counter with one
				fail += 1    

		# if fail is equal to zero

		# print You Won
		if fail == 0:        
			print ("You won this game wohoo!!!")
			inp()
			

		# exit the script
			break              

		print("")

		# ask the user go guess a character
		guess = input("guess a character:") 

		# set the players guess to guesses
		guesses += guess                    

		# if the guess is not found in the secret word
		if guess not in word:  
	 
		 # turns counter decreases with 1 (now 9)
			turns -= 1        
	 
		# print wrong
			print ("Wrong guess")    
	 
		# how many turns are left
			print ("You have", + turns, 'more guesses left !') 
	 
		# if the turns are equal to zero
			if turns == 0:           
		
			# print "You Loose"
				print ("Ohh ! You Loose")
				print("Better luck next time..")
				inp()
				
	
		
def nam():       #name of player is entered..
	name = input("What is your name? ")
	if name.isalpha():       #condition checked for accurate name input
		

		print ("Hello, " + name, "lets have some brain storm and play hangman!")
		print("")
		print("-----")
		print("|   |")
		print("|   0")
		print("| /-+-\ ") 
		print("|   |") 
		print("|   |") 
		print("|  | |") 
		print("|  | |") 
		print("|")
		print("--------")
		print("")

		print ("Are You Ready ??")
		for x in range(1,4):
			print(x)
			time.sleep(1)
			
		hang()         #hang means function which include game...is called.
	else:
		print("enter your correct name sir/madam!")           #in case of wrong choice nameis entered again..
		nam()
	



#welcoming the user
nam()


