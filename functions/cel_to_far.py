def convert(c):
    return (c * 9 / 5) + 32

def main():
    cel = float(input("Enter Celsius :: "))

    fahrenheit = convert(cel)

    print("Fahrenheit =", fahrenheit)

if __name__ == "__main__":
    main()