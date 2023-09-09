1. wap to find greater number among two number

n1=int(input("enter the 1st number:"))
n2=int(input("enter the 2nd number:"))
n3=int(input("enter the 3rd number:"))

if n1>n2 and n1>n3 :
	print(n1," is the greatest")
elif n2>n3 and n2>n1:
	print(n2,"is the greatest")
else:
	print(n3,"is the greatest")
