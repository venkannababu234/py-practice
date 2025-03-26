def prod(number):
    pro=1
    for numbers in number:
        pro*=numbers
    return pro

l=[1,1,2,3,4,5,7]
print('product of all numbers is ',prod(l))