#Simple print program
print("Hello Guru")

#print with provided input
name = input("What is your name ?")
print("Hello", name)

#input accept String, if it a number then int() fn mut be ued
#age = input("What is your age ?")
#print(age + 5)

#input() along with int() fn for numbers
age = int(input("What is your age ?"))
print(age+5)

#how input() behaves when numbrs are entered
number = input("Enter a number: ")
print(number + number)

#how python behave with "String" & +
a = "5"
b = "5"
print(a+b)

##how python behave with "non-String" & +
a = 5
b = 10
print(a+b)

#if else condition
age = int(input("Enter your age :"))
if age >= 18 :
    print("Eligible")
else :
    print("Not Eligible") 

#elif condition
mark = int(input("Enter your Score"))
if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 70:
    print("Grade C")
else:
    print("Grade D")