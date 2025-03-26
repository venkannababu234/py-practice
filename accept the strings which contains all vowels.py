str1=input('enter any string').lower()
vowels=set('aeiou')
if vowels.issubset(set(str1)):
    print('yes the string contains all the vowels')
else:
    print('no')