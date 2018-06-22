#q1 wap to calculate the area of parallelogram.


class Shape:
	def __init__(self,length,height,ang1,ang2,ang3,ang4):
		self.length=length
		self.height=height
		self.ang1=ang1
		self.ang2=ang2
		self.ang3=ang3
		self.ang4=ang4
	def area(self):
		self.result=self.length*self.height
		
class Para(Shape):
	def pararesult(self):
		print("area of real parallelogram=",self.result,"sq. units")
		print("parallelogram has equal opposite angles.")
		
class Rect(Shape):
	def rectresult(self):
		print("area of parallelogram which is actually rectangle:",self.result,"sq. units")
		print("all angles of rectangle are 90 each.")
		
class rhom(Shape):
	def rhomresult(self):
		print("area of rhombus is:",self.result,"sq. units")
		print("only opposite sides of rhombus are equal.And if you have opposite angles equal it becomes a square.")
		
		
length=int(input("enter length:"))
height=int(input("enter height:"))
ang1=int(input("enter angle 1:"))
ang2= 180-ang1
print("ang2=",ang2)
ang3=int(input("enter angle 3:"))
ang4=180-ang3
print("ang4=",ang4)
print("")
print("")
print("(ang1,ang3),(ang2,ang4) are pairs of opposite angles")

a=Para(length,height,ang1,ang2,ang3,ang4)
b=Rect(length,height,ang1,ang2,ang3,ang4)
c=rhom(length,height,ang1,ang2,ang3,ang4)

if ang1==ang3 and ang2==ang4 
	a.area()
	print("")
	a.pararesult()
elif ang1==ang2==ang3==ang4==90:
	b.area()
	print("")
	b.rectresult()
else:
	c.area()
	print("")
	c.rhomresult()
