balance = float(0)

# deposit balance
def deposit(balance, amount):
    amount = float(input("Enter the Deposite Amount :: "))
    balance += amount
    return balance

def  withdraw(balance, amount):
    amount = float(input("Enter the Withdraw Amount :: "))
    if balance >= amount:
        balance -= amount
        print("Withdraw amount Done")
        return balance
    else:
        print("Withdraw Amount does not Possible")
        return balance

# check balance
def check_balance(balance):
    print("Current Balance is ::", balance)
    return balance

# set pin
correct_pin = input("Enter your 4-digit PIN :: ")

attempt = 0
amount = float(0) 

def main():
    while attempt < 3:
        pin = input("Enter PIN :: ")
        if correct_pin == pin:     # compare pin code with correct_pin 
            print("correct PIN login")
            print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
            choice = int(input("Enter your Choice :: "))

            if choice == 1:
                balance =  deposit(balance, amount)

            elif choice == 2:
                balance = withdraw(balance, amount)

            elif choice == 3:
                balance = check_balance(balance)

            elif choice == 4:
                print("Exit")
                exit()

            else:
                print("Invalid choice")
                break
        else:
            print(" Wrong PIN")
            attempt += 1      # increase attempt
            print("Attempts used", attempt)
        
            if attempt == 3:
                print("Exit Program")
                exit()
    
if __name__ == "__main__":
    main()
