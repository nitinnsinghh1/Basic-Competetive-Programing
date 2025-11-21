n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):
            sum+=arr[k]
        print(sum)
        sum=0
