#!/usr/bin/env python3

# 1. Type conversions
print(int(3.75))
print(float("123"))
print(bool(0))
print(str(False))

# 2. String to uppercase
x = "hello"
print(x.upper())

# 3. Calculate z and convert to integer
x = 5
y = 3.14
z = x + y
print(f"z = {z}, type: {type(z).__name__}, as integer: {int(z)}")

# 4. String operations
s = 'hello'
print(s.upper())
print(s.replace('e', 'a'))
print(s.startswith('he'))
print(s.endswith('lo'))