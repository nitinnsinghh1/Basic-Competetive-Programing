n= int (input())
if (n>0 and n <=500):
    A = list(map(int,input().split()))
    if (n==len(A)):
        for i in A:
            if(i % 2==0):
                print(i,end=" ")
    else:
        print("Length out of limits!!")
else:
    print("Length out of bound")