print("Simple Calculator")
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Choose an operation: "))

    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print("Result:", num1 + num2)
        elif choice == 2:
            print("Result:", num1 - num2)
        elif choice == 3:
            print("Result:", num1 * num2)
        elif choice == 4:
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print("Result:", num1 / num2)

    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
