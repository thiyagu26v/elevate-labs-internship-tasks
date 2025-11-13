def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("===== Simple Calculator =====")

while True:
    print("\nChoose operation:")
    print("1. + (Addition)")
    print("2. - (Subtraction)")
    print("3. * (Multiplication)")
    print("4. / (Division)")
    print("5. Exit")

    choice = input("\nEnter choice (+, -, *, / or 5 to exit): ")

    if choice == "5":
        print("Exiting... Goodbye!")
        break

    if choice not in ["+", "-", "*", "/"]:
        print("Invalid choice! Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "+":
        print("Result:", add(num1, num2))
    elif choice == "-":
        print("Result:", subtract(num1, num2))
    elif choice == "*":
        print("Result:", multiply(num1, num2))
    elif choice == "/":
        print("Result:", divide(num1, num2))
