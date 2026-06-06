import json

FILE_NAME = "company.json"

def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def company_info(data):
    print("Company Information")
    print(data["company"]["name"])
    print(data["company"]["founded"])
    

    print("\nThe Headquarter is in ",data["company"]["offices"]["headquarters"]["city"], data["company"]["offices"]["headquarters"]["country"]) 

    print("\nThis Branch is in ", data["company"]["offices"]["branches"][0]["city"],"\nThe Total Employees is :: ",data["company"]["offices"]["branches"][0]["employees_count"]) 

    print("\nThe other Branch is in ", data["company"]["offices"]["branches"][1]["city"],"\nThe Total Employees is :: ",data["company"]["offices"]["branches"][1]["employees_count"],"\n") 

def update_comp(data):
    print("Company Name :: ",data["company"]["name"] )
    new_name = input("Enter the Company New Name :: ")
    data["company"]["name"] = new_name
    print("Company Name Saved Successfully....")
    
    save_data(data)

def employee_info(data):
    
    print("Employee Name is :: ",data["company"]["employees"][0]["name"],"\nskills is ", data["company"]["employees"][0]["skills"][0],",",data["company"]["employees"][0]["skills"][1],"and",data["company"]["employees"][0]["skills"][2])

    print("Project is ", data["company"]["employees"][0]["projects"][0]["name"],"and it is ",data["company"]["employees"][0]["projects"][0]["status"])

    print("Project is ", data["company"]["employees"][0]["projects"][1]["name"],"and it is ",data["company"]["employees"][0]["projects"][1]["status"])


    print("\n\nEmployee Name is :: ",data["company"]["employees"][1]["name"],"\nskills is ", data["company"]["employees"][1]["skills"][0],"and",data["company"]["employees"][1]["skills"][1])


    print("Project is ", data["company"]["employees"][1]["projects"][0]["name"],"and it is ",data["company"]["employees"][1]["projects"][0]["status"], "\n")

def update_emp(data):
    user_id = int(input("Enter The ID of Employee :: "))
    employee_list = data["company"]["employees"]

    for employee in employee_list:
        if employee["id"] == user_id:
            print("Employee Name :: ",employee["name"])
            new_name = input("Enter the Employee New Name :: ")
            employee["name"] = new_name
            print("Employee Name Saved Successfully....")
    
    save_data(data)

def main():
    data = load_data()

    while(True):
        print("1. Company Info\n2. Employee Info\n3. Exit")
        choice = int(input("Enter Your Choice :: "))

        if choice == 1:
            print("1.View Company info\n2.Update Company info")
            choose = int(input("Enter Your Choice :: "))

            if choose == 1:
                company_info(data)
            elif choose == 2:
                update_comp(data)
            else :
                print("Invalid choice")

        elif choice == 2:
            print("1.View Employee info\n2.Update Employee info")
            var = int(input("Enter Your Choice :: "))

            if var == 1:
                employee_info(data)
            elif var == 2:
                update_emp(data)
            else :
                print("Invalid choice")

        elif choice == 3:
            print("Exit")
            exit()

        else :
            print("Invalid Choice")

if __name__ == "__main__":
    main()