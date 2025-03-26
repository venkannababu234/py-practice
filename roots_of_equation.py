import math
a=float(input('enter a value'))
b=float(input('enter a value'))
c=float(input('enter a value'))
discr=b**2-4*a*c
if discr==0:
    roots=-b/(2*a)
    print('roots are',roots)
elif discr>0:
    root1=(-b+math.sqrt(discr))/(2*a)
    root2=(-b-math.sqrt(discr))/(2*a)
    print('roots are',root1,root2)
else:
    real=-b/(2*a)
    imaginary=math.sqrt(discr)/(2*a)
    print('Roots are:', f"{real} + {imaginary}i,", f"{real} - {imaginary}i")



