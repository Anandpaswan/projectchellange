def calculator():
    while True:
        # Print options for the user
        print("Enter '1' to add two numbers")
        print("Enter '2' to subtract two numbers")
        print("Enter '3' to multiply two numbers")
        print("Enter '4' to divide two numbers")
        print("Enter '5' to end the program")
        
        # Get user input
        user_input = input(": ")

        # Check if the user wants to quit
        if user_input == "5":
            break
        # Check if the user input is a valid operator
        elif user_input in ["1", "2", "3", "4"]:
            # Get first number
            num1 = float(input("Enter a number: "))
            # Get second number
            num2 = float(input("Enter another number: "))

            # Perform the operation based on the user input
            if user_input == "1":
                result = num1 + num2
                print(num1, "+", num2, "=", result)

            elif user_input == "2":
                result = num1 - num2
                print(num1, "-", num2, "=", result)

            elif user_input == "3":
                result = num1 * num2
                print(num1, "*", num2, "=", result)

            elif user_input == "4":
                result = num1 / num2
                print(num1, "/", num2, "=", result)
        else:
            # In case of invalid input
            print("Invalid Input")

# Call the calculator function to start the program
calculator()