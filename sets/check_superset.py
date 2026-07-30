set_a = set(map(int, input("Enter The Set :: ").split()))
n = int(input("Enter The Number :: "))
set_b = set(map(int, input("Enter The Set :: ").split()))
set_c = set(map(int, input("Enter The Set :: ").split()))

if set_a.issuperset(set_b):
    if set_b.issuperset(set_c):
        print("True")
    
print("False")