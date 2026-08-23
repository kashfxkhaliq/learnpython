def convert_inches_to_cm(inches):
    cm = inches * 2.54
    return cm

# Main program
def main():
    print("Height Converter (Inches to Centimeters)")
    
    inches_input = float(input("Enter your height in inches: "))
    cm_result = convert_inches_to_cm(inches_input)
    print(f"{inches_input} inches is equal to {cm_result:.2f} centimeters.")

# Run the program
if __name__ == "__main__":
    main()