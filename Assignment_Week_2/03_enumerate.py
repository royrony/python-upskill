
# 1. Using below list and enumerate(), print index followed by value. 
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)

# 2. Using below dict and enumerate, print key followed by value
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# 3. Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], 
# use enumerate() to create a list of tuples where each tuple contains the index 
# and the corresponding fruit, but only for even indices.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
even_indexed = [(i, fruit) for i, fruit in enumerate(fruits) if i % 2 == 0]
print(even_indexed)