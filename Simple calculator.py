# A menu driven program to perform basic arithmetic operations

def menu():
    print("----Simple Calculator----")
    print("1. Addtion")
    print("2. Subtaction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice(1-5):")

    if choice in ['1', '2', '3', '4']:
        # get two numbers from the user
        try:
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter your second number:"))
        except ValueError:
            print("Invalid input please enter numeric values.")
            continue

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result:{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result:{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not alloed.")
        else:
            print(f"Result:{num1} / {num2} = {num1 / num2}")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")