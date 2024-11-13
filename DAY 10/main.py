from replit import clear
from calculator_art import art

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def divide(a, b):
    return a / b
def multiply(a, b):
    return a * b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear()
    print(art)
    a = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    continue_calculation = True
    answer = a
    while continue_calculation:   
        a = answer
        operator = input("Pick an operation: ")  
        b = float(input("What's the next number? "))
        calculate = operations[operator]
        answer = calculate(a, b)
        print(f"{a} {operator} {b} = {answer}")
        if input(f"Type 'y' to continue clculating with {answer}, or type 'n' to start anew calculation: ") == "y":
            continue_calculation = True
        else :
            continue_calculation = False
    calculator()
    
calculator()