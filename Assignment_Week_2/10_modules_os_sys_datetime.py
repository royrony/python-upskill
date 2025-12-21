# Modules - os, sys, datetime
import os
import datetime
from datetime import timedelta

# 1. Using datetime, add a week and 12 hours to a date.
original_date = datetime.datetime(2020, 3, 22, 10, 0)
new_date = original_date + timedelta(weeks=1, hours=12)
print(f"Original: {original_date}")
print(f"New: {new_date}")

# 2. Code to get the dates of yesterday, today, and tomorrow.
today = datetime.date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

# 3. Write a code snippet using os module
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Create folder "test"
os.makedirs("test", exist_ok=True)
print("Created 'test' folder")

# List all files and folders
print("Files and folders:")
for item in os.listdir(current_dir):
    print(item)

# Remove the directory "test"
os.rmdir("test")
print("Removed 'test' folder")

# 4. Write a Python program to rename a file from old_name.txt to new_name.txt.
try:
    os.rename("old_name.txt", "new_name.txt")
    print("File renamed successfully")
except FileNotFoundError:
    print("old_name.txt not found")

# 5. Create a file and Write a Python program to get the size of a file named example.txt
with open("example.txt", "w") as f:
    f.write("This is an example file.")

file_size = os.path.getsize("example.txt")
print(f"Size of example.txt: {file_size} bytes")

# 6. Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
date_string = "Feb 25 2020 4:20PM"
date_obj = datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(date_obj)

# 7. Subtract 7 days from the date 2025-02-25 and print the result.
date = datetime.date(2025, 2, 25)
new_date = date - timedelta(days=7)
print(f"New date: {new_date}")

# 8. Format the date 2020-02-25 as "Tuesday 25 February 2020"
date = datetime.date(2020, 2, 25)
formatted_date = date.strftime("%A %d %B %Y")
print(formatted_date)