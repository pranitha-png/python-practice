def Fibo(N):
    f1=0
    f2=1
    f3=f1+f2
    count=2
    print(f1,f2,end=' ')
    while(count<N):
        print(f3,end=' ')
        count=count+1
        f1=f2
        f2=f3
        f3=f1+f2
N=int(input("Enter the limit:"))
Fibo(N)
