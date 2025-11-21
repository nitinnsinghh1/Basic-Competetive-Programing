n=int(input())
sum=0
count=0
if(n>0 and n<1000):
    p=list(map(int,input().split()))
    k=int(input())
    if(len(p) == n):
        for i in range(0,n):
            for j in range(i+1,n):
                sum = p[i] + p[j]
                if(sum == k):
                    count+=1
        print(count)
    