import json

def main():

    while(1):
        print("1. Add Stock\n2. View Stock\n3. Exit")
        choice = int(input("Enter your Choice :: "))

        if choice == 1:
            f = open("stock.json", "w")
            
            name = input("Enter the Name of Product :: ")
            stock = int(input("Enter the Stock of the Product :: "))

            values = {"name" : name , "stock" : stock}
            data = json.dumps(values)
            f.writelines(data)
            f.close()
            print("Done")

        elif choice == 2:
            f = open("stock.json", "r")
            data = f.readlines()
            print(data)
            f.close()

        elif choice == 3:
            print("Exit")
            exit()

        else :
            print("Invalid Choice ")


if __name__ == "__main__":
    main()