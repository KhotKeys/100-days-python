print("===============Welcome to Keys ATM Machine===================");

account = {
    "name": "new-user",
    "balance": 456789,
    "acc_no": 1234567890,
    "pin": 1234,
    "type": "personalaccount"
},

print("===============Welcome to Keys ATM Machine===================");

pin = input("please enter your pin to continue: \n")

if pin == account["pin"]:
    while True:
        print("Press 1 to check your balance")
        print("Press 2 to deposit your money")
        print("Press 3 to withdraw your money")
        print("Press 4 to exit")
        option = int(input("please enter an option: \n"))
        if option == 1:
            print("your balance is: ", account["balance"])
        elif option == 2:
            amount = int(input("how much would you like to deposit: \n"))
            account["balance"] = account["balance"] + amount
            print("you have successfully deposited: ", amount)
            print("your new balance is: ", account["balance"])
        
