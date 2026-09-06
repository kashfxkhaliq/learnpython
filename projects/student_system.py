import json

FILE_NAME = "student.json"

def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
# Save data to JSON
def save_data(student_list):
    with open(FILE_NAME, "w") as file:
        json.dump(student_list, file, indent=4)

# Add students
def add_list_of_student(student_list):
    name = (input("Enter Name : "))
    roll_numb = (input("Enter Roll Number : "))   
    math = int(input("Enter Math Marks : "))
    english = int(input("Enter English Marks :"))
    science = int(input("Enter Science Marks : "))
    total_marks = math + english + science
    per = total_marks / 3

# Dictionary All data save students 
    students = {
        "name": name,
        "roll_numb":roll_numb,
        "marks":[math, english, science],
        "total": total_marks,
        "percentage": per,
    
    }
    
    student_list.append(students)
    save_data(student_list)
    print("Student Add Successfully")

def  view_student_result(student_list):
    if student_list == []:
        print(" Student Result Not Found")

    else:
     print("\nStudent Result")
     for student in student_list:
        print("Name:", student["name"]) # print all data 
        print("Roll Number:", student["roll_numb"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Percentage:", student["percentage"])

def main():
      
    student_list = load_data()
    
    while True:
        print("\nMENU")
        print("1.Add Student\n2. View Student Result\n3. Save Data to File\n4.Exit")
      
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_list_of_student(student_list)

        elif choice == 2:
            view_student_result(student_list)
        
        elif choice == 3:
            save_data(student_list)
            print("Save all data in JSON file")

        elif choice == 4:
            exit()

        else:
            print("Invalid Choice")

# Run program
if __name__ == "__main__":
    main()
            