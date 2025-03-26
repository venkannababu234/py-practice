def leapyear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return 'yes'
    else:
        return 'not'

year=int(input('enter any year'))
print(leapyear(year))