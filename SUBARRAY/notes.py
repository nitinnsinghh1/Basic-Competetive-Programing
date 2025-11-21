# #given an array elements every element repeats twice except 1.Find uniques element 
# ans=0
# a=[2,9,2,9,3]
# for i in range(len(a)):
#     ans=ans^a[i]
# print(ans)

#Right shift operator
#         8 4 2 1
# a=10    1 0 1 0 10=10=10/20 
# a>>1    0 1 0 1 5=10/2=10/2^1
# a>>2    0 0 1 0 2
# a>>3    0 0 0 1 1
# n=43210 n=21 i=2
#given an integer n how many set bits count how many set bit are there in n
'''
n=int(input())
count=0
n1=bin(n)
print(n1)
for i in n1:
    if n&1:       
        count += 1
    n=n>>1
print(count)
'''
#given n array of n integers where all numbers occur an even no of times except 1 which occurs odd no of times find that no
#line of theinput contains integer n denoting the size of the array next line of the n space seperated integers denoting the elements of array.
'''
ans=0
a=[2,9,2,9,3]
for i in range(len(a)):
    ans=ans^a[i]
print(ans)
'''
#given a astring calculate the length of longest pallindromic substring 
# example:

str1 = input()
length = len(str1)
ans = "" 
for i in range(length):
    for j in range(i, length):
        l1 = str1[i:j+1]   
        if l1 == l1[::-1]: 
            if len(l1) > len(ans):
                ans = l1
print(len(ans))

#given a number n and index i print the ith bit of n 
#n=30 i=2 output=1