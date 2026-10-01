num = int(input("Enter number of your choice:"))
if num%2 == 0: 
    print("The number is even")
else:
    print("The number is odd")

num = int(input("Enter number of your choice:"))
if num < 0:
    print("The number is negative")
    if num%2 == 0: 
        print("The number is even")
    else:
        print("The number is odd")
elif num > 0:
    print("The number is poitive")
    if num%2 == 0: 
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is zero")