#own program for calculations
N=int(input("Enter how many numbers:"))
print('''Enter the operation you want to do
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division''')
option=int(input("Enter the option:"))
if(option==1):
    count=0
    for i in range(N):
        n=int(input("Enter the number:"))
        count=count+n
    print("The sum of the numbers are:")
    print(count)
elif(option==2):
    num=0
    for i in range(N):
        n1=int(input("Enter the number:"))
        num=num-n1
    print("Subtraction=",num)
elif(option==3):
    mul=1
    for i in range(N):
        n2=int(input("Enter the number:"))
        mul=mul*n2
    print("Multipication=",mul)
elif(option==4):
    print("Only two numbers for division")
    n3=int(input("Enter the first number:"))
    n4=int(input("Enter the second number:"))
    d=n3/n4
    print("Division=",d)
else:
    print("Invalid option!")

