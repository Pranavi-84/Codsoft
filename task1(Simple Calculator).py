choice = input("Enter your choice (1-4): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Addition:")
        result = num1 + num2
        print("Result:", result)
    elif choice == '2':
        print("Subtraction:")
        result = num1 - num2
        print("Result:", result)
    elif choice == '3':
        print("Multiplication:")
        result = num1 * num2
        print("Result:", result)
    elif choice == '4':
        print("Division:")
        result = num1 / num2
        print("Result:", result)
    else:
        if num2 == 0:
            print("Error: Cannot divide by zero")
else:
    print("Invalid choice")
