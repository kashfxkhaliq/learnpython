start = int(input("Enter the Start Number :: "))
end = int(input("Enter the End Number :: "))

sum = 0
for num in range(start, end + 1):
    sum = sum + num ** 2
print("The Sum of Squares is :: ", sum)