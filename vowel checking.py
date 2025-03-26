char=input('enter charecter')

if len(char)==1 and char.isalpha():
    char.lower()
    if char in 'aeiou':
        print('vowel')
    else:
        print('not a vowel')

else:
    print('invalid input')