# Student Management System using Functions

students = []  # List to store student data

# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    student = {
        "Name": name,
        "Age": age,
        "Grade": grade
    }
    
    students.append(student)
    print(f"\n {name} has been added successfully!\n")

# Function to display all students
def display_students():
    if not students:
        print("\n No student records found!\n")
        return
    
    print("\n Student Records:")
    print("-" * 30)
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['Name']} - Age: {student['Age']}, Grade: {student['Grade']}")
    print("-" * 30)

# Function to search for a student by name
def search_student():
    search_name = input("Enter student name to search: ")
    
    found_students = [s for s in students if s["Name"].lower() == search_name.lower()]
    
    if found_students:
        print("\n Student Found:")
        for student in found_students:
            print(f" {student['Name']} - Age: {student['Age']}, Grade: {student['Grade']}")
    else:
        print(f"\n No student named '{search_name}' found!\n")

# Function to update student details
def update_student():
    search_name = input("Enter student name to update: ")
    
    for student in students:
        if student["Name"].lower() == search_name.lower():
            print("\n Student Found! Enter new details:")
            student["Age"] = int(input("Enter new age: "))
            student["Grade"] = input("Enter new grade: ")
            print(f"\n {student['Name']}'s record updated successfully!\n")
            return

    print(f"\n No student named '{search_name}' found!\n")

# Function to delete a student
def delete_student():
    search_name = input("Enter student name to delete: ")
    
    global students
    students = [s for s in students if s["Name"].lower() != search_name.lower()]
    
    print(f"\n Student '{search_name}' has been removed (if existed).\n")

# Function to display menu
def show_menu():
    print("\n🎓 Student Management System")
    print("1️ Add Student")
    print("2️ Display Students")
    print("3️ Search Student")
    print("4️ Update Student")
    print("5️ Delete Student")
    print("6️ Exit")

# Main function to run the program
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\n Exiting program. Goodbye!")
            break
        else:
            print("\n Invalid choice! Please enter a number between 1 and 6.\n")

# Run the program
if __name__ == "__main__":
    main()
