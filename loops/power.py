base = int(input("Enter a Base Number :: "))
exponent = int(input("Enter a Exponent Number :: "))
result = 1
i = 1
while i <= exponent:
    result *= base
    i += 1
print(f"{base} raised to the power of {exponent} is: {result}")