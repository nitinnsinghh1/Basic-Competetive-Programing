n=int(input())
l=[]
order=list(map(int,input().split()))
for i in order:
    if (i%5 == 0):
        l.append(i)
l.reverse()
print(l)