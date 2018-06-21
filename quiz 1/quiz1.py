#question 1  have name and age as input from user and tell him in which year he will be 100 years old.

name = input("enter your name")
age = int(input("enter your age"))
if(age>=100):
	print("congo! ypu reached the 100 year mark!")
else:
	x = 100-age      #to calculate remaining years
	y = x+18         #to cal year with reference to current year
	z = 2000+y       #to cal actual year in which person will turn 100
	print(name,"you will be 100 years old in the year:",z)





 #question 2 wap which will find all such numbers which are divisible by 7 but are not a multiple of 5 bw(2000,3200)both included the numbers obtained should be printed in a comma separated sequence on a single line.

l=[]
for x in range(2000,3201): 
	if x%7==0 and x%5!=0:
		l.append(x)
print(l)

#question 3 wap which accepts comma separated input. and generate a list and a tuple which contains every number.


lis=input("enter the numbers and put comma after each number:\n")

lis=lis.split(",")  #entered string type or comma separated input is divided into list
tup=tuple(lis) #*lis #tuple(lis)

print(lis)
print(tup)



#question 4 wap that accepts the sentence and cal the number of uppercase and lower case letters.
s=input("enter the sentence")
l = 0
u = 0

for w in s:
	if w.isupper():
		u = u + 1
	elif w.islower():
		l = l + 1
		
print("Number of lower case are %d, and upper case are %d"%(l,u))
 
