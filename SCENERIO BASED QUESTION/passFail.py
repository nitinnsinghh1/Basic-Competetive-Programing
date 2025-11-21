n= int (input())
if(n>0 and n<=1000):
    A = list(map(int,input().split()))
    if (n == len(A)):
        pass_count=0
        fail_count=0
        for i in A:
            if(i>=35):
                pass_count+=1
            else:
                fail_count+=1
        print(pass_count,fail_count)
    else:
        print("Length out of limits!!")
else:
    print("Out of bound!!")