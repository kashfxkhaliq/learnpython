n = int(input("Enter The Number :: "))
Eng_sub = set((map(int,input("Enter The Number :: ").split())))
b = int(input("Enter The Number :: "))
Fre_sub = set((map(int,input("Enter The French Subcriber :: ").split())))

Per_sub = Eng_sub.intersection(Fre_sub)
count = len(Per_sub)
print(count)