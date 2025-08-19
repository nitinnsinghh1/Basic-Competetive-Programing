a= int(input("Enter your percentage"))
if a>100:
    print("wrong percentage")
elif a>=85:
    print("A+")
elif 65<=a<85:
    print("A")
elif 45<=a<65:
    print("B")
elif 25<=a<45:
    print("C")
elif  25<a<=0:
    print("D")