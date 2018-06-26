import math                         #math module is imported to perform certain tasks with functions defined in it.


def menu():                                    #menu is displayed to have a choice for performing any operation.
	print("")
	print("<------------MENU------------->")
	print("")
	print("1.Addition")
	print("2.Subtraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Raise to power")
	print("6.Floor division")
	print("7.Ceil division")
	print("8.Factorial")
	print("9.Squareroot")
	print("10.Exit")
	print("")
	x=input("enter your choice=")      #choice is inputed from user.
	if x.isdigit():                     #condition is checked for having digit as a choice.
		x=int(x)                        #default input string is converted into int.
		if x==1:
			add()                       #add() is called
		elif x==2:
			sub()                       #sub() is called
		elif x==3:
			mul()                       #mul() is called
		elif x==4:
			div()                       #div() is called
		elif x==5:
			power()                     #power() is called
		elif x==6:
			flrdiv()                    #flrdiv() is called
		elif x==7:
			ceildiv()                   #ceildiv() is called
		elif x==8:
			fact()                      #fact() is called
		elif x==9:
			square()                    #square() is called
		else:
			if x==10:
				print("Thanks! visit again!")                  #execution is exit
			else:
				print("")
				print("enter correct choice->")                 #on wrong input choice is entered again
				print("")
				menu()			
	else:
		print("")
		print("enter correct choice->")
		print("")
		menu()
	
#1	
def add():
	a=input("enter the first number=")
	b=input("enter the second number=")
	if a.isdigit() and b.isdigit():
		sum=int(a)+int(b)                    #sum is calculated
		print("result=",sum)                  #sum is displayed
	else:
		print("input again..")                #wrong input 
		add()
	print("do you want to add again?")          #user is asked to perform same task again 
	
	p=input("if yes then press Y/y else press any key!")       #on yes add() is called again
	if p=="Y" or p=="y":
		add()
	else:
		menu()              #on no choice is asked again 

#2 
def sub():
	a=input("enter the first number=")
	b=input("enter the second number=")
	if a.isdigit() and b.isdigit():
		diff=int(a)-int(b)            #subtraction
		print("result=",diff)
	else:
		print("input again..")
		sub()
	print("do you want to subtract again?")
	
	p=input("if yes then press Y/y else press any key!")
	if p=="Y" or p=="y":
		sub()
	else:
		menu()
		
#3
def mul():
	a=input("enter the first number=")
	b=input("enter the second number=")
	if a.isdigit() and b.isdigit():
		mult=int(a)*int(b)                     #multiplication
		print("result=",mult)
	else:
		print("input again..")
		mul()
	print("do you want to multiply again?")
	
	p=input("if yes then press Y/y else press any key!")
	if p=="Y" or p=="y":
		mul()
	else:
		menu()
		
#4
def div():
	a=input("enter the first number=")
	b=input("enter the second number=")
	if a.isdigit() and b.isdigit():
		try:
			division=int(a)/int(b)			#division
		except Exception as e:
			print(e)
		else:
			print("result=",division)
	else:
		print("input again..")
		div()
	print("do you want to divide again?")
	
	p=input("if yes then press Y/y else press any key!")
	if p=="Y" or p=="y":
		div()
	else:
		menu()
		
#5
def power():
	a=input("enter the first number=")
	b=input("enter the second number=")
	if a.isdigit() and b.isdigit():
		math.pow(int(a),int(b))                    #with pow()func of math module power is cal
		print("result=",math.pow(int(a),int(b)))
	else:
		print("input again..")
		power()
	print("do you want to raise to power again?")
	
	p=input("if yes then press Y/y else press any key!")
	if p=="Y" or p=="y":
		power()
	else:
		menu()
		
#6 
def flrdiv():
	a=input("enter the first number=")
	b=input("enter the second number=")
	if a.isdigit() and b.isdigit():
		try:
			floor_division=int(a)//int(b)			#division
		except Exception as e:
			print(e)
		else:
			print("Floor Division result=",floor_division)    #with floor func of math module floor value of division is cal
	else:
		print("input again..")
		flrdiv()
	print("do you want to divide again with result as floor value?")
	
	p=input("if yes then press Y/y else press any key!")
	if p=="Y" or p=="y":
		flrdiv()
	else:
		menu()
		
#7
def ceildiv():
	a=input("enter the first number=")
	b=input("enter the second number=")
	if a.isdigit() and b.isdigit():
		try:
			division=int(a)/int(b)			#division
		except Exception as e:
			print(e)
		else:
			print("ceil Division result=",math.ceil(division))       #with ceil func of math module ceil value of division is cal
	else:
		print("input again..")
		ceildiv()
	print("do you want to divide again with result as ceil value?")
	
	p=input("if yes then press Y/y else press any key!")
	if p=="Y" or p=="y":
		ceildiv()
	else:
		menu()
		
#8
def fact():
	a=input("enter the number=")
	if a.isdigit():
		math.factorial(int(a))                #factorial is cal
		print(" Factorial is =",math.factorial(int(a)))
	else:
		print("input again..")
		fact()
	print("do you want to find factorial again?")
	
	p=input("if yes then press Y/y else press any key!")
	if p=="Y" or p=="y":
		fact()
	else:
		menu()
		
#9
def square():
	a=input("enter the number=")
	if a.isdigit():
		math.sqrt(int(a))               #squareroot is cal
		print(" Squareroot of entered number is =",math.sqrt(int(a)))
	else:
		print("input again..")
		square()
	print("do you want to find squareroot again?")
	
	p=input("if yes then press Y/y else press any key!")
	if p=="Y" or p=="y":
		square()
	else:
		menu()
	
	
	
print("Hello! welcome you on my mathematical bureau!")           #welcome note
print("")
print("How can i help you out of your maths problem..")
print("")

menu()    #menu is called to have first choice.

	
	
	
	
	

