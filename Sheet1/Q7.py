a= int(input("Enter First Side"))
b= int(input("Enter Second Side"))
c= int(input("Enter Third  Side"))
if a+b+c==180:
    if a==90 and b==90 and c==90:
        print("Right angle triangle")
elif a>90 or b>90 or c>90:
    print("Obtuse Angle")
else:
    print("Acute Angle")