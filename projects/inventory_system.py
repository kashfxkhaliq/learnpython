import json

FILE_NAME = "inventory.json"

def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
# Save data to JSON
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_product(data):
    id = int(input("Enter The ID :: "))
    name = input("Enter The Name :: ")
    price = int(input("Enter The Price :: "))
    quantity = int(input("Enter The Quantity :: "))

   
    new_products =  {
            "id": id,
            "name": name,
            "price" : price,
            "quantity" : quantity
            }
    data["products"].append(new_products)
    save_data(data)
    print("Products Add Successfully")


def view_product(data):

    for product in data["products"]:
        print(f"ID is : {product['id']} \nName is : {product['name']} \nPrice is : {product['price']} \nQuantity is : {product['quantity']}")
    
def update_product(data):
        
    product_list = data["products"]

    user_id = int(input("Enter The ID :: "))

    for product in product_list:
        if int(product["id"]) == user_id:
           product["name"] = (input("Enter The Name :: ")) 
           product["price"] = int(input("Enter The Price :: "))
           product["quantity"] = int(input("Enter The Quantity :: "))
           save_data(data)
           print("Product Update Successfully ") 
           break

def delete_product(data):
    id = int(input("Enter The ID :: "))
    for product in data["products"]:
        if product["id"] == id:
            data["products"].remove(product)
            print(f"Product with ID {id} has been deleted.")
            save_data(data)
            print("Delete Data Successfully")
            return
        
def total_inventory_cost(data):
    total_cost = 0

    for product in data["products"]:
        total_cost += product["price"] * product["quantity"]

    print(f"\nTotal Inventory Cost = {total_cost}")
    save_data(data)

                         
def main():

    while True:

        data = load_data()

        print("MENU")
        print("1.Add Products")
        print("2.View Products")
        print("3.Update Products")
        print("4.Delete Products")
        print("5.Total Inventory Cost")
        print("6.Exit")

        choice = int(input("Enter The Choice :: ")) 

        if choice == 1:
            add_product(data)

        elif choice == 2:
           
            view_product(data)

        elif choice == 3:
            update_product(data)

        elif choice == 4:
            delete_product(data)
            
        elif choice == 5:
            total_inventory_cost(data)

        elif choice == 6:
            exit()
            
        else:
            print("Invalid choice")

# Run program
if __name__ == "__main__":
    main()
            