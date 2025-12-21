
# 1. Find the Maximum and Minimum Values in a List
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print(f"Maximum: {max(numbers)}, Minimum: {min(numbers)}")

# 2. Given a set of numbers, find the maximum and minimum values.
setn = {5, 10, 3, 15, 2, 20}
print(f"Set Maximum: {max(setn)}, Set Minimum: {min(setn)}")

# 3. Write a Python function that takes a list of strings as input and returns a tuple 
# containing the shortest and longest word from the list, in that order.
def find_shortest_longest(words):
    shortest = min(words, key=len)
    longest = max(words, key=len)
    return (shortest, longest)

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = find_shortest_longest(words)
print(result)