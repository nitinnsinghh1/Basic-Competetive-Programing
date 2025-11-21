n=int(input())
for i in range(n):
    st=input()
    vowelcount=0
    consonentcount=0
    for i in st:
        if(i in["a","e","i","o","u","A","E","I","O","U"]):
            vowelcount+=1
        else:
            consonentcount+=1
    print(vowelcount,consonentcount)