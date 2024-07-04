#Q7 Create a program that prints the multiplication table of a given number using a while loop.
num=int(input("Enter the number: "))
i=1
while i<=10:
    print(num,"*",i,"= ",num*i)
    i+=1
