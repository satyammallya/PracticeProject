no=int(input("enter the number:"))
ones=int(no%10)
no=no/10
tens=int(no%10)
no=no/10
hundreds=int(no%10)
thousands=int(no/10)
print("Reverse:",ones,tens,hundreds,thousands)

SHORTCUT FOR REVERSING A STRING:

no=int(input("enter the number:"))
print(no[::-1])
#the above code will not run because the variable is of integer type

no=input("enter the number:")
print(no[::-1])
#the above code will run because the variable is of String type


