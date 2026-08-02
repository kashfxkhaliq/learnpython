list_a = list(map(int, input("Enter the list of integers: ").split()))
list_b = list(map(int, input("Enter the list of integers: ").split()))
common_items = []

for item in list_a:
    if item in list_b:
        common_items.append(item)

print("Common Elements in List are :", common_items)