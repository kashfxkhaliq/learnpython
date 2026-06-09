# Function Addition
def add(a: int, b: int) ->int:
    result = a + b
    return result

# Function Subtraction
def sub(a: int, b: int) ->int:
    result =  a - b
    return result

#Function Multiplication
def mul(a: int, b: int) ->int:
    result = a * b
    return result

# Functin division
def div(a: int, b: int) ->float:
    result = a / b
    return result

# Function Modulus
def mod(a: int, b: int) ->int:
    result = a % b
    return result

# Function Exponentiation
def exp(a: int, b: int) ->int:
    power =  a ** b
    return power

# Funtion Main
def main():

 while True:
        print("\nMenu")
        print("1.Addition\n2.subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponentiation\n7.Exit")

        choice = int(input("Enter The Choice :: "))
        
        a = int(input("Enter The Number :: "))
        b = int(input("Enter The Number :: "))

        if choice == 1:
            sum = add(a, b)
            print("Addition of Two Numbers is ::", sum)

        elif choice == 2:
            subtract = sub(a, b)
            print("subtraction of Two Numbers is ::", subtract)

        elif choice == 3:
            multiply = mul(a, b)
            print("Multiplication of Two Numbers is ::", multiply)

        elif choice == 4:
            if b == 0:
                print("Infinite")
            else:
                divide = div(a, b)
                print("Division of Two Numbers is ::", divide)

        elif choice == 5:
            if b == 0:
                print("Cannot take modulus with zero")
            else:
                modulus = mod(a, b)
                print("Modulus of Two Numbers is ::", modulus)

        elif choice == 6:
            power = exp(a, b)
            print("Exponentiation of Two Numbers is ::", power)

        elif choice == 7:
            exit()

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()