#elif condition tempature
temp = int(input("Enter current tempature :"))
if temp > 35:
    print("Hot")
elif temp > 25:
    print("Warm")
elif temp > 15:
    print("Cool")
else:
    print("Cold")

age = int(input("Enter your age :"))
if age <= 10:
    print("Kids- Not Eligible for vote")
elif age < 18: 
    print("Teens- Not Eligible for vote")   
else :
    print("Eligible") 

number = int(input("Enter any number"))
if number > 0:
    print("Number is Positive")
elif number < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

mark = int(input("Enter your Score"))
if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 70:
    print("Grade C")
elif mark >= 60:
    print("Grade D")    
else:
    print("Fail")    