n=int(input())
arr=list(map(int,input().split()))
sum=0
sum1=0
l=[]
for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):
            sum+=arr[k]
        l.append(sum)
        sum=0
for i in l:
    sum1+=i
print(sum1)