n=int(input("Enter number"))
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print("_",end=" ")
    for h in range(i):
        print("*",end=" ")
    print()