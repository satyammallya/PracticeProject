    #Q. armstrong number between 100 to 2000
def armstrong(num):
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp =temp// 10

    if num == sum:
        return True
    else:
        return False
 
for num in range(100,2001):    
    RESULT=armstrong(num)
    if RESULT==True:
        print(num," is armstrong")
    else:
        print(num," is not armstrong")
