str1=input('enter any string')
l=len(str1)//2
str2=str1[:l].upper()+str1[l:len(str1)]
print(str2)
str3=str1[0].upper()+str1[1:len(str1)-1]+str1[len(str1)-1].upper()
print(str3)