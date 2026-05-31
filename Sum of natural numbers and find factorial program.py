def Fact(N):
    if(N==0 or N==1):
        return 1
    else:
        return (N*Fact(N-1))
def SumN(N):
    if(N==0):
        return 0
    else:
        return (N+SumN(N-1))
print("1:To find factorial of number, 2:To find sum of natural numbers, 3:Exit")
option=int(input("Enter the option:"))
if(option==1):
    N=int(input("Enter an integer number:"))
    print("Factorial of",N,"is", Fact(N))
elif(option==2):
    N=int(input("Enter an integer number:"))
    print("Sum of natural humbers upto",N,"is",SumN(N))
else:
    print("Invalid option")
