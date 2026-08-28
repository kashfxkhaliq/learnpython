import json
from datetime import datetime

FILE_NAME = "data.json"


# Load data from JSON
def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save data to JSON
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Authenticate user
def login(data):
    username = input("Enter username: ")
    pin = input("Enter PIN: ")

    if (username in data["users"]) and (data["users"][username]["pin"] == pin):
        print("Login successful!")
        return username
    else:
        print("Invalid username or PIN")
        return None


# Deposit function
def deposit(data, user):
    amount = float(input("Enter amount to deposit: "))
    data["users"][user]["balance"] += amount

    time = datetime.now()
    transaction = f"{time} - Deposited: {amount}"
    data["users"][user]["transactions"].append(transaction)

    save_data(data)
    print("Deposit successful!")


# Withdraw function
def withdraw(data, user):
    amount = float(input("Enter amount to withdraw: "))

    if amount > data["users"][user]["balance"]:
        print("Insufficient balance!")
        return

    data["users"][user]["balance"] -= amount

    transaction = f"{datetime.now()} - Withdrawn: {amount}"
    data["users"][user]["transactions"].append(transaction)

    save_data(data)
    print("Withdrawal successful!")

# Check balance
def check_balance(data, user):
    balance = data["users"][user]["balance"]
    print(f"Your balance is: {balance}")


# View transactions
def view_transactions(data, user):
    print("Transaction History:")
    transactions = data["users"][user]["transactions"]
    for t in transactions:
        print(t)


# Main program
def main():
    data = load_data()

    user = login(data)
    if not user:
        return

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            deposit(data, user)
        elif choice == "2":
            withdraw(data, user)
        elif choice == "3":
            check_balance(data, user)
        elif choice == "4":
            view_transactions(data, user)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
