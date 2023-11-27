from art import logo

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-":substract,
    "*":multiply,
    "/":divide
}

print(logo)

num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

shouldQuit = False
while not shouldQuit:

    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    check = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit")
    if check.lower() == "n":
        print("Good luck.")
        shouldQuit = True
    else:
        num1 = answer
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
