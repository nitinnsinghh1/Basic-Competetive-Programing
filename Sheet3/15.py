n=int(input("Enter limit"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
for k in range(n,0,-1):
    for l in range(k):
        print("*",end="")
    print()