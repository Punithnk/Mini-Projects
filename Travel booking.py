# Travel booking program
# This program allows users to book travel packages for Goa, Thirupathi, and Ooty.

def goa():
    print("Goa package is 10,000 per person.")
    var = input("Do you want to book this package? (yes/no): ")
    if var.lower() == "yes":
        per_person = 10000
        fullname = input("Enter full name: ")
        while True:
            try:
                while True:
                    try:
                        age = int(input("Enter your age: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid integer for age.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for your age.")
            try:
                age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for age.")
        number_of_persons = int(input("Enter number of persons: "))
        total_amount = per_person * number_of_persons
        if total_amount >= 50000:
            offer_total_amount = total_amount - 5000
            print(f"Hi {fullname}, your Goa trip is booked. Your bill is more than 50,000 so 5000 discount applied. Total amount to pay is {offer_total_amount}.")
        else:
            print(f"Hi {fullname}, your Goa trip is booked. Total amount to pay is {total_amount}.")
    else:
        print("Thank you for considering our Goa package.")

def thirupathi():
    print("Thirupathi package is 5000 per person.")
    var = input("Do you want to book this package? (yes/no): ")
    if var.lower() == "yes":
        per_person = 5000
        fullname = input("Enter full name: ")
        age = int(input("Enter your age: "))
        number_of_persons = int(input("Enter number of persons: "))
        total_amount = per_person * number_of_persons
        print(f"Hi {fullname}, your Thirupathi trip is booked. Total amount to pay is {total_amount}.")
    else:
        print("Thank you for considering our Thirupathi package.")

def ooty():
    print("Ooty package is 15,000 per person.")
    var = input("Do you want to book this package? (yes/no): ")
    if var.lower() == "yes":
        per_person = 15000
        fullname = input("Enter full name: ")
        age = int(input("Enter your age: "))
        number_of_persons = int(input("Enter number of persons: "))
        total_amount = per_person * number_of_persons
        print(f"Hi {fullname}, your Ooty trip is booked. Total amount to pay is {total_amount}.")
    else:
        print("Thank you for considering our Ooty package.")

def display_menu():
    print("----WELCOME TO THE GREEN BUS----")
max_attempts = 10
attempts = 0

while attempts < max_attempts:
    display_menu()
    choice = input("Enter your choice (1/2/3) or 'exit' to quit: ")
    if choice == '1':
        goa()
    elif choice == '2':
        thirupathi()
    elif choice == '3':
        ooty()
    elif choice.lower() == 'exit':
        print("Thank you for using our service. Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.")
    attempts += 1

if attempts >= max_attempts:
    print("Maximum attempts reached. Exiting the program.")
    print("Thank you for using our service. Have a great day!")
# End of the travel booking program