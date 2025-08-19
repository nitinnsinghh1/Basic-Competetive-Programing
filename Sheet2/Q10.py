a=int(input("enter Your Number"))
a1=a
b=0
c=0
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
if (a1==b):
    print("palindrome")
else:
    print("Not")