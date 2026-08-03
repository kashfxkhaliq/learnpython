# Function for Addition
def add(a: int, b: int) -> int:
    return a + b


# Function for Subtraction
def sub(a: int, b: int) -> int:
    return a - b


# Function for Multiplication
def mul(a: int, b: int) -> int:
    return a * b


# Function for Division
def div(a: int, b: int):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Function for Modulus
def mod(a: int, b: int) -> int:
    return a % b


# Function for Exponentiation
def exp(a: int, b: int) -> int:
    return a ** b


# Function for Square
def square(x: int) -> int:
    return x ** 2


# Function for Cube
def cube(x: int) -> int:
    return x ** 3


# Main Function
def main():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Square")
        print("8. Cube")
        print("9. Exit")

        choice = input("Enter your choice [1 to 9] :: ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            a = int(input("Enter the first number :: "))
            b = int(input("Enter the second number :: "))

            if choice == "1":
                print("Addition is = ", add(a, b))
            elif choice == "2":
                print("Subtraction is = ", sub(a, b))
            elif choice == "3":
                print("Multiplication is = ", mul(a, b))
            elif choice == "4":
                print("Division is = ", div(a, b))
            elif choice == "5":
                print("Modulus is = ", mod(a, b))
            elif choice == "6":
                print("Exponentiation is = ", exp(a, b))

        elif choice == "7":
            x = int(input("Enter a number :: "))
            print("Square is = ", square(x))

        elif choice == "8":
            x = int(input("Enter a number :: "))
            print("Cube is = ", cube(x))
        
        elif choice == "9":
            print("Exit")
            exit()

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()