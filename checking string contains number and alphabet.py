str1=input('enter any string')
has_letter=False
has_number=False
for char in str1:
    if char.isalpha():
        has_letter=True
    if char.isdigit():
        has_number=True
    if has_number and has_letter:
        break
if has_number and has_letter:
    print('True')
else:
    print('False')
