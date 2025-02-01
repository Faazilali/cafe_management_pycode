def check_balance():
    print(f"Current balance: {balance}₹")

def deposit():
    deposit = float(input("Enter depositing amount: ₹"))
    if(deposit <= 0):
        print("Invalid amount")
        return 0
    else:
        return deposit

def withdraw():
    withdraw = float(input("Enter the amount of withdrawal: ₹"))
    
    if(withdraw > balance):
        print("No sufficient balance for withdrawal.")
        return 0
    elif(withdraw <= 0):
        print("Invalid withdrawal amount.")
        return 0
    else:
        return withdraw
        

if __name__ == '__main__':
    balance = 0
    is_true = True
    
    while is_true:
        print("*******************************")
        print("Welcome to the Bank Management.....")
        print("*******************************")
        print("Choose your option:\n1.Check balance\n2.Deposit money\n3.Withdraw money\n4.Exit")
        print("*******************************")

        user = input("Enter your choice: ")
        user.lower()
        
        if(user == 'check balance'):
            check_balance()

        elif(user == 'deposit money'):
            balance += deposit()

        elif(user == 'withdraw money'):
            balance -= withdraw()
            
        elif(user == 'exit'):
            is_true = False

        else:
            print("Enter a valid choice from above.....")
        
        print()
    print("Thank you have a nice day.")
    print()