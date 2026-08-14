def km_to_miles(km):
    return km * 0.621371

def main():
    km = float(input("Enter kilometers: "))
    print(km_to_miles(km))

if __name__ == "__main__":
    main()