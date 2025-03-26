str1=input('enter any string')
words=str1.split()
reversed_string=""
for word in reversed(words):
    reversed_string+=word+" "

print(reversed_string)