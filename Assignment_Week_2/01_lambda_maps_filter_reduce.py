from functools import reduce

# 1. Given a list let's see how to double each element of the given list. Using map() 
a = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, a))
print(doubled)

# 2. Use filter() and lambda to extract all even numbers from a list of integers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 3. Use reduce() and lambda to find the longest word in a list of strings.
words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest_word)

# 4. Use map() to square each number in the list and round the result to one decimal place.
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
squared_rounded = list(map(lambda x: round(x ** 2, 1), my_floats))
print(squared_rounded)

# 5. Use filter() to select names with 7 or fewer characters from the list.
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filtered_names = list(filter(lambda name: len(name) <= 7, my_names))
print(filtered_names)

# 6. Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]
numbers_sum = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers_sum)
print(total)