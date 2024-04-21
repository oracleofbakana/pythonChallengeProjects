
def multiply(n1, n2):
    return n1 * n2


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "*": multiply,
    "+": add,
    "-": subtract,
    "/": divide
}


def calculator():
    num1 = float(input("What is the first number?\n"))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = str(input("Enter the symbol of operation you wish to perform:\n"))
        num2 = float(input("What is the next number? \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:") == "y": num1 = answer
        else:
            should_continue = False
            calculator()
