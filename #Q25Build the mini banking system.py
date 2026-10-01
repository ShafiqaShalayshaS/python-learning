#Q25 - Build the mini banking system using while,if/elif/else, input, int,%,break,a counter/
#accumukator and changing balance.No lists, functions, for loops, max/min
old_balance = 10000
Deposit=0 
Withdraw=0 
Amount_sent= 0 
Accumulator=0
count = 0
new_balance = old_balance
print ("1. Deposit")
print ("2. Withdraw")
print ("3. Check balance")
print ("4. Send Money")
print ("5. Exit")
opt= int(input("Choose: "))
while opt != 0:
    if opt == 1:
        opt1 = int(input("Enter amount: "))
        if(opt1%100==0):
            new_balance = new_balance + opt1
            count+=1
            Deposit=Deposit+opt1
        #new_balance = Check_balance
        else:
            print("Please enter amount in multiples of 100")
    elif opt == 2:
        opt2 = int(input("Enter amount: "))
        if opt2 <= new_balance:
            if(opt2%100==0):
                new_balance = new_balance - opt2
                count+=1
                Withdraw=Withdraw+opt2
            else:
                print("Please enter amount in multiples of 100")    
        else:
            print("Withdrawal amount higher than actual balance")
    elif opt == 3:
        print("Balance: ",new_balance)
    elif opt == 4:
        opt3 = int(input("Enter amount: "))
        if opt3 <= new_balance:
            if(opt3%100==0):
                new_balance = new_balance - opt3
                count+=1
                Amount_sent=Amount_sent+opt3
            else:
                print("Please enter amount in multiples of 100")
        else:
            print("insuffient balance")    
    elif opt>5:
        print("Invalid Option")
    else:
        print("Exit")
        print("total transacation",count)
        Accumulator=Deposit+Withdraw+Amount_sent
        print("Total amount accumulated in transaction",Accumulator)
        break
    print ("1. Deposit")
    print ("2. Withdraw")
    print ("3. Check balance")
    print ("4. Send Money")   
    print ("5. Exit")
    opt= int(input("Choose: "))
#if opt==5:
    #print("Exit")






 


