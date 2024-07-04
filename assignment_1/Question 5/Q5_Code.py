#Q5. Create a program that checks if a given year is a leap year.
year=int(input("Enter the year: "))
if(year%4): 
    print("It is not a leap year.")
else:
    print("It is a leap year.")