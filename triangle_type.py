l=int(input('enter the length'))
b=int(input('enter the breath'))
h=int(input('enter height'))

if l==b==h:
    print('equilateral')
elif l==b or b==h or l==h:
    print('issocseles')
else:
    print('scalene')