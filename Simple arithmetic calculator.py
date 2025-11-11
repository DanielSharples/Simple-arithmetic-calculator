# Simple Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error, can't divide by zero."
    return a / b

def format_result(result):
    # Only show decimals if needed
    if isinstance(result, (int, float)) and result == int(result):
        return int(result)
    return result

print("Simple arithmetic calculator")
print("Choose operation:")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", format_result(add(num1, num2)))
elif choice == '2':
    print("Result:", format_result(subtract(num1, num2)))
elif choice == '3':
    print("Result:", format_result(multiply(num1, num2)))
elif choice == '4':
    print("Result:", format_result(divide(num1, num2)))
else:
    print("Invalid input")
