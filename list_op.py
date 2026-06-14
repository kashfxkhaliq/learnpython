
students = ["Aliza", "Fariha", "Yusra", "Dua", "Zoya"]

add_student = input("Enter the Add Student Name :: ")
students.append(add_student)

students.sort() # arrange the names with alphabets

print(students)

remove_student = input("Enter the Remove Student Name :: ")

if remove_student in students:
    students.remove(remove_student)
    
else:
    print("Student Name Not Found in List")
    
students.reverse()

print("Final List is", students)

