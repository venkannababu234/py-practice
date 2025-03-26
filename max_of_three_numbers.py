a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))

if a>b and a>c:
    print('a is large')
elif b>c and b>a:
    print('b is large')
else:
    print('c is large')