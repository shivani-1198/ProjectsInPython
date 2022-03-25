def Calculator(operation):
    operation = int(operation)

    num1 = raw_input("Enter first number: ")
    num1 = int(num1)

    num2 = raw_input("Enter second number: ")
    num2 = int(num2)

    if operation == 1:
        # code for Add
        print("The sum is " + str(num1 + num2))

    elif operation == 2:
        # code for Sub
        print("The difference is " + str(num1 - num2))

    elif operation == 3:
        # code for Mult
        print("The multiplication is " + str(num1 * num2))

    elif operation == 4:
        # code for Div
        print("The division is " + str(num1 / num2))
        
    else:
        print("Invalid Entry")



print("Welcome to my calculator")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVISION")
print("Select a Operation to perform: \n")

operation = raw_input()
Calculator(operation)
