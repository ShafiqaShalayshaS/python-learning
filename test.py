num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))
num3 = int(input("Enter Number 3:"))
if num1 >= num2 and num1 >= num3:
    print("The largest number is", num1)
elif num3 >= num2 and num3 >= num1:
    print("The largest number is", num3)
else:
    print("The largest number is", num2)