
balance = float(0)
trans_type = 0
trans_amt = float(0)
#trans_balance = 0

def receipt(type , amount, bal):

    print("------Receipt------")
    print("Transaction type is : ", type)
    print("Your Transaction amount is :: ", amount)
    print("Your Current balance is :: ", bal)


def deposit(trans_amt , balance):
     
    trans_amt = float (input("Enter Your Deposit Amount ::"))
    balance += trans_amt
    return balance , trans_amt

def withdraw(trans_amt , balance):
   
    trans_amt = float (input("Enter the Withdraw Amount :: "))
    if balance >= trans_amt:
        balance -= trans_amt
        print("Transaction Done")
        return balance , trans_amt
    else :
        print("Transaction does not Possible")
        return balance , 0
    

def main():

# Menu
    while (1):
        print("------Menu------")
        print("1. Deposit \n 2. Withdraw \n 3.View Last Transaction \n 4. Exit ")
        choice = input("Enter Your Choice :: ")
        if choice == "1":
            trans_type = "deposit"
            balance , trans_amt = deposit(trans_amt , balance) 
        
        elif choice == "2":
            trans_type = "Withdraw"
            balance , trans_amt  = withdraw(trans_amt , balance)

        elif choice == "3":
            receipt(trans_type , trans_amt, balance)
        
        elif choice == "4":
            exit()
        else :
            print("Invalid Choice")

    

if __name__ == "__main__":
    main()

