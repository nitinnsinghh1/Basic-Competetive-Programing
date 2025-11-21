n=int(input())
price=list(map(int,input().split()))
count=0
max=price[0]
for i in price:
    if(i>max):
        max=i
        count+=1
print(count)