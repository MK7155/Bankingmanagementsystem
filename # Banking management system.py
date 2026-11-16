# Banking management system

def main():
    print("===== Welcome to the Banking Management System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Creating a New Bank Account")

    elif choice == "2":
        print("User Login")

    elif choice == "3":
        print("Check Account Balance")

    elif choice == "4":
        print("Deposit Money")

    elif choice == "5":
        print("Withdraw Money")

    elif choice == "6":
        print("Thank you for using our Banking Management System!")

    else:
        print("Invalid Choice!")

if __name__ == "__main__":
    main()
    

