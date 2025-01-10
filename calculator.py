from ascii_art import logo

def input_number(input_text):
    while True:
        try:
            number = int(input(input_text))
        except:
            print("This is not a number!")
        else:
            break
    return number

def input_operator():
    while True:
        operator = input("Enter mathematical operator:\n+\n-\n*\n/\n")
        if not (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
            print("This isn't an operator!")
        else:
            break
    return operator

def input_continue_answer():
    while True:
        answer = input("Do you want to continue with previous result? Type 'y' if yes. Type 'n' if you want to start over. Type 'q' to quit: ")
        if not (answer == "y" or answer == "n" or answer == "q"):
            print("Wrong answer!")
        else:
            break
    return answer

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)

continue_calculate = "n"
first_number = 0

while True:
    if continue_calculate == "n":
        first_number = input_number("Enter first number: ")
    operator = input_operator()
    second_number = input_number("Enter second number: ")
    result = calculations[operator](first_number, second_number)
    print(f"Result: {result}")
    continue_calculate = input_continue_answer()
    if continue_calculate == "y":
        first_number = result
    elif continue_calculate == "n":
        print("\n" * 10)
        print(logo)
    elif continue_calculate == "q":
        break