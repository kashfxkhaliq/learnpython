num = int(input("Enter The Number :: "))
s = set(map(int, input("Enter The Set :: ").split()))
commands = int(input("Enter The Number :: "))

for i in range(commands):
    command = input("Enter The Choice :: ").split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
    else:
        pass
    
print(sum(s))
