n=int(input())
for i in range(n):
    st=input().split()
    strev=st[::-1]
    print(strev)
    if st==strev:
        print("1")
    else:
        print("0")
