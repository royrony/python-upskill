#!/usr/bin/env python3

# 1. Max and min from list
nums = [1, 2, 3, 4, 5]
print(f"Max: {max(nums)}, Min: {min(nums)}")

# 2. Merge lists
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a + b)

# 3. Count occurrences
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
print(a.count(3))

# 4. Sort list
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]
print(sorted(a))

# 5. Add to set
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)

# 6. Remove from set
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)

# 7. Set intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)

# 8. Count in tuple
fruits = ('apple', 'banana', 'apple', 'cherry')
print(fruits.count('apple'))

# 9. Concatenate tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)

# 10. Access dictionary value
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["age"])

# 11. Add to dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
person["gender"] = "M"
print(person)

# 12. Remove from dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
del person["city"]
print(person)

# 13. Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print({**dict1, **dict2})