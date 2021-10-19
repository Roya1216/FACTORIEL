import math 
number = int(input("Enter your number to check if it is factorial or not : "))
def check(num):
    if num == 2 or num == 1:
         return True
    else:
        for i in range(0, int(num/2)):
            if num == math.factorial(i):
                return True
                break
            



if check(number) == True:
    print('yes')
else :
    print('no')