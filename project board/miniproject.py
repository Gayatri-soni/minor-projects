
def agemale():                            #function defined for checking age criteria for males
	print("Enter your age!")
	age=input("->")                        
	if len(age)>1 and age.isdigit():
		age=int(age)                       #if age entered is a digit then converted into integer and then conditions applied
		if age>20:
			print("Congrats!you are eligible for Python Fundamental course..")
		else:
			print("Agh! you seem ineligible..complete 20 springs first:)")
	else:
		print("Sorry!enter your age again")
		agemale()	                            #in case wrong input function is called again to take correct input
			
			
def agefem():                               #function for female age checking
	print("Enter your age!")
	age=input("->")
	if len(age)>1 and age.isdigit():
		if int(age)>19:
			print("Congrats!you are eligible for Core Java course..")
		else:
			print("Agh! you seem ineligible..complete 20 springs first:)")
	else:
		print("Sorry!enter your age again")
		agefem()

			
def malenam():                               #function defined for inputing name of males
	print("Enter your good name :)")
	name=input("->")
	if  name.isalpha():                       #entered name is correct then 
		print(name,"Sir!hope you are doing well..Go for Acadview to have wings!!")
		print("Enter your age!")            
		age=input("->")
		if len(age)>1 and age.isdigit():                          
			if int(age)>20:
				print("Congrats!you are eligible for Python Fundamental course..")
			else:
				print("Agh! you seem ineligible..complete 20 springs first:)")
		else:
			print("Sorry!enter your age again")
			agemale()
	else:
		print("kindly enter your accurate name please..")       #incase incorrect input func called again
		malenam()
		
def femalenam():                         #for female name input
	print("")
	print("Enter your good name :)")
	name=input("->")
	if  name.isalpha():
		print(name,"Mam!hope you are doing well..Go for Acadview to have wings!!")	
		print("Enter your age!")
		age=input("->")
		if len(age)>1 and age.isdigit():
			if int(age)>19:
				print("Congrats!you are eligible for Core Java course..")
			else:
				print("Agh! you seem ineligible..complete 20 springs first:)")
		else:
			print("Sorry!enter your age again")
			agefem()
	else:
		print("kindly enter your accurate name please..")
		femalenam()
	
	
print("************************************************")
print("")
print("hello there! We welcome you on the board!")
print("")
print ("Before enrolling you have to give some details...")
print("")
print("")
print("<-----------lets get started!---------->")
print("")
print("enter your gender pleaze")
print("if you are male kindly press M/m or if you are a female kindly press F/f")
gender=input("->")

if gender== "m" or gender== "M":             #gender is checked if male then this code is executed
	print("Hello Sir!thanks for input.")
	print("")
	print("Enter your good name :)")
	name=input("->")
	if  name.isalpha():
		print(name,"Sir!hope you are doing well..Go for Acadview to have wings!!")
		print("Enter your age!")
		age=input("->")
		if len(age)>1 and age.isdigit():
			if int(age)>20:
				print("Congrats!you are eligible for Python Fundamental course..")
			else:
				print("Agh! you seem ineligible..complete 20 springs first:)")
		else:
			print("Sorry!enter your age again")
			agemale()
	else:
		print("kindly enter your accurate name please..")
		malenam()
	
		
	
	
	
	
elif gender== "f" or gender== "F":               #if female is on board
	print("Hello Mam!thanks for input.")
	print("")
	print("Enter your good name :)")
	name=input("->")
	if  name.isalpha():
		print(name,"Mam!hope you are doing well..Go for Acadview to have wings!!")	
		print("Enter your age!")
		age=input("->")
		if len(age)>1 and age.isdigit():
			if int(age)>19:
				print("Congrats!you are eligible for Core Java course..")
			else:
				print("Agh! you seem ineligible..complete 20 springs first:)")
		else:
			print("Sorry!enter your age again")
			agefem()
	else:
		print("kindly enter your accurate name please..")
		femalenam()
	
		
		
else:
	print("oops! you pressed the wrong key! Kindly follow the given instructions carefully!")
	
	#if user is pressing wrong key in place of entering gender..then execution will start again after this message.