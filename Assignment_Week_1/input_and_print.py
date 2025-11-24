#!/usr/bin/env python3

# 1. Greet user
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2. Basic arithmetic
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")

# 3. Split names
names_input = input("Enter names separated by commas: ")
names_list = names_input.split(',')
print([name.strip() for name in names_list])

# 4. Voting eligibility
age = int(input("Enter your age: "))
print("Eligible to vote" if age >= 18 else "Not eligible to vote")

# 5. F-string formatting
value = 3.14159
print(f"{value:.2f}")