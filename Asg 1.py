tasks = []  # List to store tasks

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed_task = tasks.pop(task_no - 1)
                print(f"Task '{removed_task}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("\nExiting... Have a productive day!")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")
