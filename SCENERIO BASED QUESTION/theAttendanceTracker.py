n=int(input())
n2=list(map(int,input().split()))
c1=[]
c=0
for i in n2:
    if i==0:
        c+=1
    else:
        c1.append(c)
        c=0
max=c1[0]
for i in c1:
    if (i>max):
        max=i
print(max)