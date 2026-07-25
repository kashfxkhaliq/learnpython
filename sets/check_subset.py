# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input("Enter The Number :: "))

for i in range(t):
    a = int(input("Enter The Number :: "))
    a_set = set(map(int, input("Enter The Set :: ").split()))

    b = int(input("Enter The Number :: "))
    b_set = set(map(int, input("Enter The Set :: ").split()))

    if a_set.issubset(b_set):
        print(True)
    else:    
        print(False)

