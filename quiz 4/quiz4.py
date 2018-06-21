#q1 wap to display examination schedule.Extract date from exam_st_date.

import datetime
from datetime import date

class Date:
	def __init__(self,year,month,day):
		self.day=day
		self.year=year
		self.month=month
		
		
class Exam(Date):
	def exam_st_date(self):
		self.d=datetime.date(self.year,self.month,self.day)
		print("Examination will start from=",self.d)
	
day=int(input("enter the day"))
month=int(input("enter the month"))
year=int(input("enter the year"))
print("")	


a=Exam(year,month,day)
a.exam_st_date()
