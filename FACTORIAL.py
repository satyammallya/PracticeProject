no=int(input("Enter the number to find it's factorial:"))
factorial=1
i=1
for i in range(1,no+1):
	factorial=i*factorial
print(factorial)