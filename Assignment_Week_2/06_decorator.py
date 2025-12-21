import time
import functools

# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator 
# to that function to calculate the start and end time.
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)
    return numbers

append_numbers()

# 2. Create a parameterised decorator retry that retries a function a specified number of times.
def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == times - 1:
                        raise e
            return None
        return wrapper
    return decorator

@retry(3)
def may_fail(name):  
    print(f"Hello, {name}!")

# 3. Create a decorator validate_positive for below function
def validate_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("Argument must be positive")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):  
    return x ** 0.5

# 4. Create a decorator cache that caches the result of a function based on its arguments.
def cache(func):
    cached_results = {}
    def wrapper(x):
        if x in cached_results:
            return cached_results[x]
        result = func(x)
        cached_results[x] = result
        return result
    return wrapper

@cache
def expensive_computation(x):  
    print("Performing computation...")  
    return x * x  

expensive_computation(5)
expensive_computation(5)

# 5. Create a decorator requires_permission
def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if 'admin' in user.get('permissions', []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper

@requires_permission
def delete_user(user, user_id):  
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}  
user2 = {'name': 'John', 'permissions': ['dev']}  
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 123)
delete_user(user2, 456)