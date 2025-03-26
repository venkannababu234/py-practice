str1=input('enter any string')
str2=str1.replace(' ','')
print(str2)
words=str1.split()
for word in words:
    if len(word)%2==0:
        print(word)


