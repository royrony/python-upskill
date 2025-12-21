
# 1. Define a class Person with attributes name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(f"Name: {person.name}, Age: {person.age}")

# 2. Write a Python class named BankAccount
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

account = BankAccount("123456", "John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()

# 3. Create a class Book with a class method from_string()
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(", ")
        return cls(title, author)

book = Book.from_string("Python Programming, John Doe")
print(f"Title: {book.title}, Author: {book.author}")

# 4. Create a base class Animal with a method sound()
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())

# 5. Write a code to perform multiple inheritance.
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Animal, Flyable, Swimmable):
    def sound(self):
        return "Quack!"

duck = Duck()
print(duck.sound())
print(duck.fly())
print(duck.swim())