class Calculator:
    # Constructor (optional)
    def _init_(self):
        print("Simple Calculator Initialized!")

    # Addition method
    def add(self, a, b):
        return a + b

    # Subtraction method
    def subtract(self, a, b):
        return a - b

    # Multiplication method
    def multiply(self, a, b):
        return a * b

    # Division method
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b


# Create an object of the Calculator class
calc = Calculator()

# Take user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", calc.add(num1, num2))
elif choice == '2':
    print("Result:", calc.subtract(num1, num2))
elif choice == '3':
    print("Result:", calc.multiply(num1, num2))
elif choice == '4':
    print("Result:", calc.divide(num1, num2))
else:
    print("Invalid choice!")