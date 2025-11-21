n=int(input())
if(n>0 and n<=1000):
    A=list(map(int,input().split()))
    max=A[0]
    min=A[0]
    if (n == len(A)):
        for i in A:
            if(i>max):
                max=i
            if(i<min):
                min=i
        print(max,min)
    else:
        print("Length out of limits!!")
else:
    print("Out of bound!!")
