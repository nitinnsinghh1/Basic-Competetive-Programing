a=int(input("Enter Year"))
if a%4==0:
    print("Leap Year")
    if a%400:
        print("Leap Year")
else:
    print("Not leap Year")