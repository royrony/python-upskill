
# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
for i in range(10):
    print(next(fib_gen))

# 2. Write a generator function called infinite_multiples(n) that yields multiples 
# of the given base value indefinitely.
def infinite_multiples(n):
    i = 1
    while True:
        yield n * i
        i += 1

multiples_gen = infinite_multiples(3)
for i in range(5):
    print(next(multiples_gen))

# 3. Write a generator function called repeat_word(word, times) that yields 
# the given word a specified number of times.
def repeat_word(word, times):
    for _ in range(times):
        yield word

word = "hello"  
times = 5
for w in repeat_word(word, times):
    print(w)