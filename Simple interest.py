def Simple(P,T,R):
    SI=float(P*T*R)
    return SI
def Compound(P,T,R):
    CI=float(P*((1+R/100)**T-1))
    return CI
P=float(input("Enter the Principle amount:"))
T=int(input("Enter the time:"))
R=float(input("Enter the rate of interest:"))
Simple_Interest=Simple(P,T,R)
Compound_Interest=Compound(P,T,R)
diff=Compound_Interest-Simple_Interest
print("Simple interest=",Simple_Interest)
print("Compound Interest=",Compound_Interest)
print("Difference of interest=",diff)
