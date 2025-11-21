A =input()
count=0 
for i in range(len(A)):
    if (A[i]=='b' and A[i+1]=='o' and A[i+2]=='b'):
        count = count+1
    print(count)