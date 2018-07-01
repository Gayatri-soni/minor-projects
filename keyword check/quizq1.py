# Ques:- 1 :- write a Python program to check an entered string is a Python keyword or not, if it is keyword print with a message and if it is not it will display all the keywords of python

import keyword

x=input("enter the string")

if keyword.iskeyword(x):
    print("entered string is a keyword!")
else:
    print("entered string is not a keyword!")

#to print list of keywords

from keyword import kwlist

print("list of python keywords=",kwlist)