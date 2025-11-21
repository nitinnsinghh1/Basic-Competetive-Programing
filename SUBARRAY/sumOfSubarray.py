n=int(input())
arr=list(map(int,input().split()))
index=list(map(int,input().split()))
sum=0
for i in range(n):
    for j in range(i,n):
        for k in range(i, j + 1):
            if arr[i]==index[0] and arr[j]==index[1]:
                sum+=arr[k]
print(sum)
 
