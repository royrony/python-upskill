#!/usr/bin/env python3

# 1. Calculate area function
def calculate_area(length, width=10):
    return length * width

print(calculate_area(5, 3))
print(calculate_area(5))

# 2. Recursive factorial
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))

# 3. Reverse string function
def reverse_string(s):
    return s[::-1]

print(reverse_string('hello'))

# 4. Sum lists function
def sum_lists(list1, list2):
    return sum(list1) + sum(list2)

a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
print(sum_lists(a, b))

# 5. Distinct sorted elements
def distinct_sorted(lst):
    return sorted(list(set(lst)))

a = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]
print(distinct_sorted(a))