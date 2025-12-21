# 1. Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
numbers = [1, 2, 3, 4, 5]
all_positive = all(x > 0 for x in numbers)
print(all_positive)

# 2. Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
numbers = [1, 3, 5, 7, 8]
any_even = any(x % 2 == 0 for x in numbers)
print(any_even)

# 3. Determine if any number in a list is divisible by 5 an print.
numbers = [1, 3, 7, 9, 15]
any_divisible_by_5 = any(x % 5 == 0 for x in numbers)
print(f"Any number divisible by 5: {any_divisible_by_5}")