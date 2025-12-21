# File Handling
import csv

# 1. Write a Python program to read the entire content of a file named sample.txt and display it.
try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("sample.txt not found")

# 2. Write a Python program to count the number of words in a file named words.txt
try:
    with open('words.txt', 'r') as file:
        content = file.read()
        word_count = len(content.split())
        print(f"Word count: {word_count}")
except FileNotFoundError:
    print("words.txt not found")

# 3. Create a program to write the string "Hello, Python!" into a file named output.txt.
with open('output.txt', 'w') as file:
    file.write("Hello, Python!")
print("Written to output.txt")

# 4. Write a Python program to create a CSV file named students.csv
data = [  
    ["Name", "Roll Number", "Marks"],  
    ["Alice", "101", "85"],  
    ["Bob", "102", "90"],  
    ["Charlie", "103", "88"]  
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file created")

# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.
def read_large_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"{filename} not found")

# Usage example
for line in read_large_file('large_file.txt'):
    print(line)