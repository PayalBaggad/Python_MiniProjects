def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {num1 + num2}")
        elif choice == '2':
            print(f"The result is: {num1 - num2}")
        elif choice == '3':
            print(f"The result is: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid Input")

calculator()


"""
Explanation:
1. The program displays a menu with arithmetic operations.
2. The user selects an operation by entering a number (1, 2, 3, or 4).
3. The program asks for two numbers.
4. Based on the chosen operation, it performs the calculation and displays the result.
5. It handles division by zero with a specific error message.
"""
