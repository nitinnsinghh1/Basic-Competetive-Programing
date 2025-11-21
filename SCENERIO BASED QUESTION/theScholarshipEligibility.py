limits=int(input("Enter number of applicants: "))
count=0
for i in range(0,limits):
    marks,Attend=list(map(int,input().split()))
    if ((marks>=75)and (Attend>=80)):
        count+=1
print(count)