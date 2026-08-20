import json

file_name = "hospital.json"

def load_data():
    with open(file_name, "r") as file:
        return json.load(file)

def save_data(data):
     with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def add_patient(data):
    id = int(input("Enter the ID :: "))
    name = input("Enter the Patient Name :: ")
    age = input("Enter the Patient Age :: ")
    disease = input("Enter the Patient Disease :: ")

    patient = {
        "id" : id,
        "name" : name,
        "age" : age,
        "disease" : disease
    }

    data.append(patient)
    print("\nPatient Added Successfully....")
    save_data(data)

def view_patient(data):
   
   for patient in data:
       print("\nID :: ", patient["id"])
       print("Name :: ", patient["name"])
       print("Age :: ", patient["age"])
       print("Disease :: \n", patient["disease"])

def search_patient(data):
    id = int(input("Enter the Patient ID :: "))

    for patient in data:
        if patient["id"] == id:
            print("\nName :: ", patient["name"])
            print("Age :: ", patient["age"])
            print("Disease :: \n", patient["disease"])

def update_patient(data):
    id = int(input("Enter the Patient ID :: "))

    for patient in data:
        if patient["id"] == id: 
            new_name = input("Enter the Patient New Name :: ") 
            new_age = input("Enter the Patient Age :: ")
            new_disease = input("Enter the Patient Disease :: ")

            patient["name"] = new_name
            patient["age"] = new_age
            patient["disease"] = new_disease
            save_data(data)
            print("Data Updated Successfully.....\n")


def delete_patient(data):
    id = int(input("\nEnter the Patient ID :: "))

    for patient in data:
        if patient["id"] == id: 
            data.remove(patient)
            print("Patient Removed Successfully...\n")
            save_data(data)
            return

    print("Patient Not Found...")



def main():

    data = load_data()
    while True:
        print("1.Add patient \n2.View Patient \n3.Search Patient \n4.Update Patient \n5.Delete Patient")
        print("6.Exit")
    
        choice = int(input("\nEnter Your Choice :: "))

        if choice == 1:
            add_patient(data)

        elif choice == 2:
            view_patient(data)

        elif choice == 3:
            search_patient(data)

        elif choice == 4:
            update_patient(data)
        
        elif choice == 5:
            delete_patient(data)

        elif choice == 6:
            print("Exit")
            exit()

        else :
            print("Invalid Choice. Try Again....")


if __name__ == "__main__":
    main()