n = int(input("Enter The Number :: "))
countries = set()

for _ in range(n):
    countries.add(input())

print(len(countries))