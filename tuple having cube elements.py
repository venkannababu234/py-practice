list1=[1,2,3,4]
tuple1=[(x,x**3)for x in list1]
print(tuple1)
tuple2=((1,2),(2,3,4),(2,5,3),(4,5),(5,6))
k=2
removed=[]
for tup in tuple2:
    if len(tup)!=2:
        removed.append(tup)

print(removed)

tuple_list = [(123, 45), (678, 90), (12, 345)]
digits=set()
for tup in tuple_list:
    for num in tup:
        for digit in str(num):
            digits.add(int(digit))

print(digits)