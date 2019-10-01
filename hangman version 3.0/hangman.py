import datetime
import time
import random
def menu():
	print("HANGMAN-The word guessing game:)-designed and developed by Gayatri(would be DECIDER!)")
	print("")
	print("------")
	print("|    |")
	print("|    0")
	print("|  /-+-\ ") 
	print("|    |") 
	print("|    |") 
	print("|   | |") 
	print("|   | |") 
	print("|")
	print("--------")
	print("")

	print ("Are You Ready ??")
	for x in range(1,4):
		print(x)
		time.sleep(1)
	print("Enter your choice !")
	print("<-------MENU------->")
	print("1.Movies ")
	print("2.Places")
	print("3.Sprituals")
	print("4.Country")
	print("5.Exit")
	x=input("choice->")
	if x.isdigit():
		x=int(x)
		if x==1:
			nam()
			movhang()
		elif x==2:
			nam()
			plhang()
		elif x==3:
			nam()
			sphang()
		elif x==4:
			nam()
			cohang()
		elif x==5:
			exit()
		else:
			print("enter choice again..")
			menu()
	else:
		print("enter choice again..")
		menu()

def inp():
	print("DO you wanna try again ?enter y or Y  and to exit press any key..")      #asking player to play again.
	x=input()
	if x=="y" or x=="Y":
		menu()		#if condition satisfied then name is asked again to start new game..
		
	else:
		print("Thanks for playing.. see you again!!")         #in case player wants to exit..
		exit()
		
def exit():                               #exit function to quit the game..
	print("Have a gud day !")
#1		
def movhang():                               #this function includes actual game to be played
	print ("Start guessing...")
	time.sleep(0.5)

	#here we set the 
	list = ["raja","darpan","bazigar","judva","neerja"]
	word=random.choice(list)
	
	
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
				
#2
def plhang():                               #this function includes actual game to be played
	print ("Start guessing...")
	time.sleep(0.6)

	#here we set the 
	list = ["kullumanali","haridwar","nainital","maclodganj","niagrafalls","shimla"]
	word=random.choice(list)
	
	#creates an variable with an empty value
	guesses = ''

	#determine the number of turns
	turns = 10
B
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
				
#3
def sphang():                               #this function includes actual game to be played
	print ("Start guessing...")
	time.sleep(0.5)

	#here we set the 
	list = ["krishna","ramayan","vishnu","bhagvatgita","mahabharat"]
	word=random.choice(list)
	
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


				
#4
def cohang():                               #this function includes actual game to be played
	print ("Start guessing...")
	time.sleep(0.5)

	#here we set the 
	list = ["america","india","england","russia","turkey"]
	word=random.choice(list)
	
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

			
		        
	else:
		print("enter your correct name sir/madam!")           #in case of wrong choice nameis entered again..
		nam()
	



#welcoming the user
menu()



