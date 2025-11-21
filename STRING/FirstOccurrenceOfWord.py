str=input()
b=input()
for i in range(len(str)):
    if(str[i]==b[0] and str[i+1]==b[1]):
        print(i)
        break