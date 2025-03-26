l1=[1,2,3,4,5]
l2=[4,5,6,7,8]

common=set(l1)&set(l2)

if common:
    print('yes there is a common elements',common)
else:
    print('no')

l3=[1,2,3,4,5,6,7,8]

common1=set(l1)&set(l2)&set(l3)

if common1:
    print('yes',common1)
else:
    print('no')