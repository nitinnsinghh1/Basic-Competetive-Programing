def fun(a):
    return a%2==0
sequence = [10, 3.5, 8, 7.2, 9, 2.0, 11.5]
filtered = list(filter(lambda x: isinstance(x, int) and fun(x), sequence))
print(filtered)