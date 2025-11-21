n=int(input())
arr=list(map(int,input().split()))
sum=0
l=[]
for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):
            sum+=arr[k]
        l.append(sum)
        sum=0
m=max(l)
print(m)
n = int(input())
arr = list(map(int, input().split()))
max_sum = current_sum = arr[0]

for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)