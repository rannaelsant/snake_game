from art import logo
print(logo)



#add
def add(num1, num2):
    return num1 + num2

#subtract
def subtract(num1, num2):
    return num1 - num2

#multiply
def multiply(num1, num2):
    return num1 * num2

#divide
def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    number_1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        number_2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(number_1, number_2)

        print(f"{number_1} {operation_symbol} {number_2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculator.: ") == "y":
            number_1 = answer
        else:
            should_continue = False
            calculator()
    '''operation_symbol = input("Pick another operation: ")
        number_3 = int(input("What's the next number?:"))
        calculation_function = operations[operation_symbol]
        second_answer = calculation_function(calculation_function(number_1, number_2), number_3)
        print(f"{first_answer} {operation_symbol} {number_3} = {second_answer}")'''

calculator()