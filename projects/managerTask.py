import json

FILE_NAME = "task.json"

def load_task():
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
# Save data to JSON
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add Task
def add_task(tasks):
    task = input("Enter The List of Tasks :: ")
    tasks.append(task)
    save_data(tasks)   
    print("Task Added to List")

def view_task(tasks):
    if not tasks:
        print("Task is not Found")
    
    else:
        print("Your Tasks")    
        for task in tasks:
            print(task)
               # incrase the task numbers

# Main menu
def main():
    tasks = load_task()
   
    while True:
        print("MENU")
        print("1.Add Task\n2.View Task\n3.Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_task(tasks)

        elif choice == 2:
            tasks = load_task()   # reload latest data
            view_task(tasks)

        elif choice == 3:
            exit()
            
        else:
            print("Invalid choice")

# Run program
if __name__ == "__main__":
    main()