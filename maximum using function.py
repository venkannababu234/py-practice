def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

num1=int(input('enter the value'))
num2=int(input('enter the value'))
num3=int(input('enter the value'))
print('maximum of three number is given by',maximum(num1,num2,num3))