year = int(input("Enter a year: "))
# Put your code here.
if year < 1582:
    print('Not within the Gregorian calendar period')
elif year % 4 != 0:
    print('Common year')
elif year % 100 != 0:
    print("Leap year, isn't divisible by 100")
elif year % 400 != 0:
    print("Common year, isn't divisible by 400")
else:
    print("it's a leap year")
