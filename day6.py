"""
a = 1
while a <= 5 :
    print(a)
    a += 1 

a = 1
while a <= 10 :
    print(a)
    a += 1 

a = 10
while a >= 1 :
    print(a)
    a -= 1   
"""
#print only even numbers
num = int(input("Enter number of your own choice :"))
a = 1
while a <= num:
    if a%2 == 0: 
        print(a)
    a += 1

#create a program until the user enter the number zero
num = int(input("Enter any number :"))
while num != 0:
    if num > 0:
        print("POSITIVE")
    else:
        print("NEGATIVE")    
    num = int(input("Enter any number :"))   


    