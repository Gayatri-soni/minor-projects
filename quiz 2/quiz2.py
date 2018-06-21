#q print a user defined list and print a new list which removes all the duplicate elements of older list.

l=[]
print("enter the numbers:")
for i in range(10):
	x=int(input())
	l.append(x)
print(l)
s=list(set(l))
print(s)