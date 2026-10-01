#Q21 - ATM Challenge
old_balance = 10000
Deposit=0 #not required
Withdraw=0 #not required
Check_balance= 0  #not required
new_balance = old_balance
print ("1. Deposit")
print ("2. Withdraw")
print ("3. Check balance")
print ("4. Exit")
opt= int(input("Choose: "))
while opt != 4:
    if opt == 1:
        opt1 = int(input("Enter amount: "))
        new_balance = new_balance + opt1
        #new_balance = Check_balance
    elif opt == 2:
        opt2 = int(input("Enter amount: "))
        if opt2 <= new_balance:
            new_balance = new_balance - opt2
        else:
            print("Withdrawal amount higher than actual balance")
    elif opt == 3:
        print("Balance: ",new_balance)
    else:
        print("Invalid Option")
    print ("1. Deposit")
    print ("2. Withdraw")
    print ("3. Check balance")
    print ("4. Exit")
    opt= int(input("Choose: "))
if opt==4:
    print("Exit")






 


