str=input()
b=int(input())
count=0
for i in str:
    if(ord(i)==b):
        count+=1
if(count>0):
    print(count)
else:
    print("Doesn't exist")
