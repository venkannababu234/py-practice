str1=input('enter any string')
vowels=set('aeiouAEIOU')
sum=0
for char in str1:
    if char in vowels:
        sum+=1

print('number of vowels are',sum)