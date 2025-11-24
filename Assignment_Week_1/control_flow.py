#!/usr/bin/env python3

# 1. Even or odd
number = int(input("Enter a number: "))
print("even" if number % 2 == 0 else "odd")

# 2. Palindrome check
def check_palindrome(s):
    return s == s[::-1]

for string in ["civic", "hello"]:
    print(f"'{string}' reversed: {string[::-1]}, palindrome: {check_palindrome(string)}")

# 3. Fibonacci sequence
n = int(input("Enter N for Fibonacci: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(fib[:n])

# 4. Find pair that sums to 9
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == 9:
            print([numbers[i], numbers[j]])
            break

# 5. Even numbers with while loop
i = 2
while i <= 20:
    print(i)
    i += 2

# 6. Find first occurrence with break
numbers = [10, 20, 30, 40, 50]
search_for = 30
for i, num in enumerate(numbers):
    if num == search_for:
        print(f"Found {search_for} at index {i}")
        break

# 7. Odd numbers with continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 8. Pass statement output
for i in range(5):
    if i == 3:
        pass
    print(i)

# 9. Match statement for weekday/weekend
day = input("Enter day of week: ").lower()
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")