num = int(input("Enter a Positive Number :: "))
fact = 1
for i in range(num, 0, -1):
    fact *= i
print(f"The Factorial of {num} is :: ", fact)