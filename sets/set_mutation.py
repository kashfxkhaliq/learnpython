# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input("Enter The Number :: "))
set_a = set(map(int, input("Enter The Set :: ").split()))
n = int(input())

for i in range(n):
    operation = input().split()[0]
    
    other_set = set(map(int, input("Enter The Set :: ").split()))
    
    if operation == "intersection_update":      
        set_a.intersection_update(other_set) 
            
    elif operation == "update":
        set_a.update(other_set)
          
    elif operation == "symmetric_difference_update":
        set_a.symmetric_difference_update(other_set)
          
    elif operation == "difference_update":
        set_a.difference_update(other_set)
    else:
        pass
        
print(sum(set_a))
        
        
    