n=int(input('enter any number'))
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print('not a prime number')

else:
    print('prime number')