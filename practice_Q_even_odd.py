def even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"

no=int(input("Enter the number:"))    
even_odd=even_odd(no)
print("The input number is :",even_odd)