def armstrong(number):
    sum = 0
    temp = number
    num_digits = len(str(number))

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp =temp// 10

    if number == sum:
        return True
    else:
        return False
 
num=int(input("Enter the number:"))       
RESULT=armstrong(num)
if RESULT==True:
    print("number is armstrong")
else:
    print("number is not armstrong")
