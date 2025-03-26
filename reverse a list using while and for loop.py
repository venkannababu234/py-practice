numbers=[1,2,3,4,5,6,7,8,9]
index= len(numbers)-1
reverse=[]
while index>=0:
    reverse.append(numbers[index])
    index-=1

print(reverse)

for i in range(index-1,-1,-1):
    reverse.append(numbers[index])

print(reverse)