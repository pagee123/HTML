print("Determine whether the input is a leap year: ")
year = input("Please enter the year: ")
rem4=int(year)%4
rem100=int(year)%100
rem400=int(year)%400
if(rem4==0):
    if(rem100!=0 or rem400==0):
        print("leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")