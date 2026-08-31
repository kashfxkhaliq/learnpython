import json
from datetime import datetime

file_name = "library.json"

# Load data
def load_data():
    with open(file_name, "r") as file:
        return json.load(file)
    

# Save data
def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

# LOGIN SYSTEM
def login(data):
    username = input("Enter username: ").strip().lower()
    pin = input("Enter PIN: ").strip()

    if username in data["users"] and data["users"][username]["pin"] == pin:
        print("\nLogin successful!\n")
        return username
    else:
        print("Invalid username or PIN!")
        return None

# SHOW BOOKS
def show_books(data):
    print("\nAvailable Books:")
    for i, book in enumerate(data["books"]):
        status = "Available" if book["available"] else "Not Available"
        print(f"{i + 1}. {book['title']} by {book['author']} - {status}")

# BORROW BOOK
def borrow_book(data, user):
    show_books(data)

    choice = int(input("\nEnter book number to borrow: ")) - 1

    if 0 <= choice < len(data["books"]):
        book = data["books"][choice] # select book

        if book["available"]:
                book["available"] = False
                data["users"][user]["borrowed_books"].append(book["title"])

                data["users"][user]["transactions"].append(
                    f"Borrowed '{book['title']}' at {datetime.now()}"
                )

                print("Book borrowed successfully")
        else:
                print("Book not available")
    else:
            print("Invalid book number")
# RETURN BOOK
def return_book(data, user):
    books = data["users"][user]["borrowed_books"] # user book list

    if not books:
        print("No books to return")
        return

    print("\nYour Borrowed Books:")
    for i, b in enumerate(books):
        print(f"{i + 1}. {b}")
        choice = int(input("Enter book number to return: ")) - 1

        if 0 <= choice < len(books):
            book_title = books.pop(choice)

            for book in data["books"]:
                if book["title"] == book_title: # list remove book 
                    book["available"] = True

            data["users"][user]["transactions"].append(
                f"Returned '{book_title}' at {datetime.now()}"
            )

            print("Book returned successfully")
        else:
            print("Invalid choice")

# VIEW BORROWED BOOKS
def view_borrowed(data, user):
    print("\nBorrowed Books:")
    if not data["users"][user]["borrowed_books"]:
        print("No books borrowed.")
    else:
        for b in data["users"][user]["borrowed_books"]:
            print("-", b)

# VIEW TRANSACTIONS
def view_transactions(data, user):
    print("\nTransaction History:")
    if not data["users"][user]["transactions"]:
        print("No transactions yet.")
    else:
        for t in data["users"][user]["transactions"]:
            print("-", t)

# MAIN PROGRAM
def main():
    data = load_data()
    user = login(data)

    if not user:
        return

    while True:
        print("\n---- MENU ----")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View Borrowed Books")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            borrow_book(data, user)
        elif choice == "2":
            return_book(data, user)
        elif choice == "3":
            view_borrowed(data, user)
        elif choice == "4":
            view_transactions(data, user)
        elif choice == "5":
            save_data(data)
            print("Goodbye")
            break
        else:
            print("Invalid choice")

        save_data(data)

# RUN PROGRAM
main()