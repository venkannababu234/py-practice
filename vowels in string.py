str1=input('enter a string')
str2='aeiouAEIOU'
count=0
for item in str1:
    if item in str2:
        count+=1

print(count)