# 1 --> Basic function Defination:
# def greet():
#     return "Hello World"
# print(greet())

# 2--> function with parammeters --> a function that takes the parameter and gives the result
# def add_numbers (a,b):
#     return a+b
# print(add_numbers(3,5))


# 3 --> Default parameters --> You can set default values for the parameters , which will be used if no arguments are provided
# def greet(name="guest"):
#     return f"Hello, {name}"
# print(greet())
# print(greet("Alice"))

# 4. --> keyword arguments --> Function can accepet arguments as kay-value of pairs , allowing flexiblity in how arguments are passed
# def print_info(name,age):
#     print(f"Name:{name},Age:{age}")
# print_info (age=25, name="Bob")

#5.--> Variable length arguments (*args And *Kwargs)
# * args : allow you to pass a varibale number of potensial arguments 
# **kwargs: Allows you to pass a variable number of keyword arguments.

# def add_all(*numbers):
#     return sum(numbers )
# print(add_all(1,2,3,4))


# def print_details (**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_details(name="Alice", age=30, city="New York")

#6. --> Return multiple values. ---> function can  return mutltiple values , which can be unpacked

# def get_coordinated():
#     return (10.0,20.0)
# x,y = get_coordinated()
# print(x,y)


#7 ---> Lambda functions (Anonymus Functions) --> lambda is a small anonymus function often used when you need a short function on the fly.
# def squre(x):
#     return x**2
# squre_lambda = lambda x: x**2
# print(squre(4))
# print(squre_lambda(4))

# #8 --> Function as preclass citizens --> in function are first class citizens, meaning they can be passed as arguments to other functions, returns from functions and assigned to variable 
# def multiply_by_two(x):
#     return x*2
# def apply_functions(func, value):
#     return func(value)
# result = apply_functions(multiply_by_two,5)
# print(result)

#9 --> HIgher order functions --> A higher order function is functiion that taken other functions as arguments or return them.
# def add_one(x):
#     return x+1
# def apply_twice(func,x):
#     return func(func(x))
# print(apply_twice(add_one,3))


#10 --> closer Inner function: ---> A closer is a function defined inside another function that remembers the values from the outer function even after the outer function has finished execusting
# def outer_function(text):
#     def innter_function():
#         return f"inner function says : {text}"
#     return innter_function

# greeting = outer_function ("hello !")
# print(greeting())

#11 --> Decoraters : ---> A decorater is a Higher order function that allows modifying the behavier of another function. they are commonly used in we frameworks
# def decorater(func):
#     def wrapper():
#         print("before function is called")
#         func()
#         print("After the function is called")
#     return wrapper
# @decorater
# def say_hello():
#     print("Hello")
# say_hello()


#12 --> Recursive function --> A function that calls itself, it's commonly used for problems like factorial,Fibonacci, And and tree traversals.

# def factorial(n):
#     if n ==1:
#         return 1
#     return n* factorial (n-1)
# print(factorial(5))

# 13--> Generator function --> Generators use Yield instead of return , producing a release of values lazily (one at a time ), which is useful for the Large dataassets
# def countdown(n):
#     while n>0:
#         yield n
#         n -=1
# for num in countdown(5):
#     print(num)

#14 --> Function Annotations --> You can provide the functions for annotations. it doesn't enforece type But it us usful for documentaion and static type checking tools 
# def add_numbers (a:int, b:int) -> int:
#     return a+b
# print(add_numbers (2,3))

#15 --> Partial functions (for functiontoosl module) - partial function is allow you to 'freeze' some portions of functions's argumnts and create a new function with fewer arguments.
# from functools import partial
# def power (base , exponet):
#     return base **exponet
# # create a new numbers funcion thats always square a function
# squre = partial(power, exponet=2)
# print(squre(5))

#16 --> Function over Loading using the dafault values --> doesn't support True function Overloading Like someLangues But you can simulate it by using Default values
# def greet(name=None):
#     if name:
#         return f"Hello,{name}!"
#     else:
#         return "Hello, Guest!"
# print(greet())
# print(greet("Tom"))

# def greet(name=None):
#     if name:
#         return f"Hello, {name}!"
#     else:
#         return "Hello, Guest!"
# print(greet())
# print(greet("Tom"))


#17 --> Unpacking arguments (*args , **kwargs): --> unpack a varible number of arguments:
# def unpacking_example(*args, **kwargs):
#     print("potensial argumsnst :",args )
#     print("keyword argumsnts ", kwargs)
# unpacking_example(1,2,3, name="jhon", age=25)