A=input()
A1=A+A
print(A1)
for i in A1:
    if (i in ["a","e","i","o","u"]):
        print("#", end="")
    elif (ord(i)>=97):
        print(i,end="")
    else:
        continue
      