# 1. Write a Python program that attempts to divide two numbers a = 10  b = 0
# and handles a ZeroDivisionError if the denominator is zero. 
a = 10
b = 0
try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

# 2. Apply exception handling to below code and handle an exception if the index is out of range.   
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print(f"Index Error: {e}")

# 3. Correct this below code with appropriate exception handlings. 
# And finally print "Execution completed"
def safe_divide(a, b):  
    try:
        result = a / b  
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid data type")

safe_divide(1, 0)  
safe_divide(1, "a")
print("Execution completed")