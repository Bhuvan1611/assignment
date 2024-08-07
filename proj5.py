year = int(input("Enter year: "))
if (year%4==0 or year%400==0):
    print(str(year)+" is a Leap Year")

else:
    print(str(year)+" is not a leap Year")
