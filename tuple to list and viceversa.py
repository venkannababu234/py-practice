tuple1=(1,2,3,7,8)
size=len(tuple1)
print(size)

list1=[4,5,6]

list1.extend(tuple1)
mytuple=tuple(list1)
print(list1)
print(mytuple)

sorted_tuple=sorted(mytuple)
l=len(mytuple)//2

min_elements=sorted_tuple[:l]
max_elements=sorted_tuple[l:len(sorted_tuple)]

print(min_elements)
print(max_elements)