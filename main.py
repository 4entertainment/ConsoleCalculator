from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return abs(n1 - n2)


# Multiply
def mul(n1, n2):
    return n1 * n2


# Divide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))

    for key in operations:
        print(key)

    flag = True

    while flag:

        operation_symbol = input("Pick an operation: ")

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
            num2 = float(input("What is the next number?: "))
        else:
            flag = False
            calculator()


calculator()
