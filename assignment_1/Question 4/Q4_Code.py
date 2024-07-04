#Write a Python program that takes an integer input from the user and prints whether the number is positive, negative, or zero. 
num=int(input("Enter the Number: "))
if num<0:
    print("The number is negative")
elif num==0:
    print("The number is zero.")
else:
    print("The number is positive.")