def printing(n):
    if n>0:
        print(n)
        printing(n-1)
n=int(input())
print(printing(n))
