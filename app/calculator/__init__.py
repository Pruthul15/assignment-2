from app.operations import addition, subtraction, multiplication, division

def calculator() -> None:
    print("Welcome to the calculator REPL! Type 'exit' to quit")
    while True:
        user_input = input("Enter: <add|subtract|multiply|divide> <num1> <num2> (or 'exit'): ")

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue

        if operation == "add":
            result = addition(num1, num2)
        elif operation == "subtract":
            result = subtraction(num1, num2)
        elif operation == "multiply":
            result = multiplication(num1, num2)
        elif operation == "divide":
            try:
                result = division(num1, num2)
            except ValueError as e:
                print(e)
                continue
        else:
            print("Unknown operation. Use: add, subtract, multiply, divide.")
            continue

        print(f"Result: {result}")
