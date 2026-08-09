def swap(a, b):
    a, b = b, a
    return a, b

def main():
    num_a = int(input("Enter a Positive Number :: "))
    num_b = int(input("Enter a Positive Number :: "))

    num_a, num_b = swap(num_a, num_b)

    print("\n After Swap:")
    print("a = ", num_a)
    print("b = ", num_b)

if __name__ == "__main__":
    main()