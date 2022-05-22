#leap year:it is divisible by 4 and remainder is 00
#and it has to be divisible by 400 and remainder is 0
year = int(input('Enter a year to check: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is a NOT leap year')
else:
    print(f'{year} is a NOT leap year')

# 0(1) because only once calculates, with one number only, there is no loop

