#!/usr/bin/env python3

# 1. Convert strings to integers
strings = ["1", "2", "3", "4", "5"]
print([int(s) for s in strings])

# 2. Filter numbers > 10
numbers = [1, 5, 13, 4, 16, 7]
print([n for n in numbers if n > 10])

# 3. Squares 1-5
print([i**2 for i in range(1, 6)])

# 4. Flatten 2D list
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
print([item for row in matrix for item in row])

# 5. Dictionary comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print({k: v for k, v in zip(keys, values)})

# 6. Filter dictionary by value
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
print({k: v for k, v in scores.items() if v > 80})