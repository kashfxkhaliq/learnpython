n = int(input("Enter The Number :: "))
Eng_sub = set((map(int,input("Enter The English Subcriber :: ").split())))
b = int(input("Enter The Number :: "))
Fre_sub = set((map(int,input("Enter The English Subcriber :: ").split())))

Per_sub = Eng_sub.symmetric_difference(Fre_sub)
count = len(Per_sub)
print(count)