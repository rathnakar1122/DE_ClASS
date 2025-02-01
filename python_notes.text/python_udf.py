1. Basic Function Definition
A simple function that takes no parameters and returns a greeting.
def greet():
    return "Hello, world!"

print(greet())  # Output: Hello, world!



2. Function with Parameters
A function that takes parameters and returns the result.
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))  # Output: 8



3. Default Parameters
You can set default values for parameters, which will be used if no arguments are provided.
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())       # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!




4. Keyword Arguments
Functions can accept arguments as key-value pairs, allowing flexibility in how arguments are passed.

def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info(age=25, name="Bob")  # Order doesn’t matter with keyword arguments









5. Variable-Length Arguments (*args and **kwargs)
*args: Allows you to pass a variable number of positional arguments.
**kwargs: Allows you to pass a variable number of keyword arguments.

# Using *args
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))  # Output: 10

# Using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
6. Return Multiple Values
Functions can return multiple values, which can be unpacked.


def get_coordinates():
    return (10.0, 20.0)

x, y = get_coordinates()
print(x, y)  # Output: 10.0 20.0
7. Lambda Functions (Anonymous Functions)
lambda is a small, anonymous function often used when you need a short function on the fly.


# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(4))        # Output: 16
print(square_lambda(4))  # Output: 16







8. Functions as First-Class Citizens
In , functions are first-class citizens, meaning they can be passed as arguments to other functions, returned from functions, and assigned to variables.


def multiply_by_two(x):
    return x * 2

def apply_function(func, value):
    return func(value)

result = apply_function(multiply_by_two, 5)
print(result)  # Output: 10
9. Higher-Order Functions
A higher-order function is a function that takes other functions as arguments or returns them.


def add_one(x):
    return x + 1

def apply_twice(func, x):
    return func(func(x))

print(apply_twice(add_one, 3))  # Output: 5
10. Closures (Inner Functions)
A closure is a function defined inside another function that remembers the values from the outer function even after the outer function has finished executing.


def outer_function(text):
    def inner_function():
        return f"Inner function says: {text}"
    return inner_function

greeting = outer_function("Hello!")
print(greeting())  # Output: Inner function says: Hello!













11. Decorators
A decorator is a higher-order function that allows modifying the behavior of another function. They are commonly used in web frameworks (e.g., Flask).


def decorator(func):
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function is called
# Hello!
# After the function is called
12. Recursive Functions
A function that calls itself. It’s commonly used for problems like factorial, Fibonacci, and tree traversals.


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

13. Generator Functions
Generators use yield instead of return, producing a series of values lazily (one at a time), which is useful for large datasets.


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # Output: 5 4 3 2 1ex
    
    
14. Function Annotations
You can provide metadata for functions using annotations. It doesn’t enforce types but is useful for documentation and static type checking tools.


def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(2, 3))  # Output: 5
15. Partial Functions (from functools module)
Partial functions allow you to "freeze" some portion of a function’s arguments and create a new function with fewer arguments.


from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a new function that always squares a number
square = partial(power, exponent=2)

print(square(5))  # Output: 25
16. Function Overloading Using Default Values
 doesn’t support true function overloading like some languages, but you can simulate it by using default values.


def greet(name=None):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, Guest!"

print(greet())       # Output: Hello, Guest!
print(greet("Tom"))  # Output: Hello, Tom!
17. Unpacking Arguments (*args and **kwargs) in Functions
You can use *args and **kwargs to pass a variable number of arguments and keyword arguments into a function.


def unpacking_example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

unpacking_example(1, 2, 3, name="John", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'John', 'age': 25}