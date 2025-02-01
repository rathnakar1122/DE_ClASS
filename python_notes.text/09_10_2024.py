#  #####################
#  Date: 09-10-2024
# #####################
# +++++++++++++++++++++++++++ 
# GCP Cloud Data Engineering:
# +++++++++++++++++++++++++++
# ####################
#   Topic: (Python)
# #################### 

# +++++++
# Agenda:
# +++++++

# 1. Python Keywords:
#     --> as, 
#         def,
#         except, 
#         finally, 
#         from, 
#         global,                 
#         import,
#         lambda, 
#         nonlocal,  
#         return, 
#         try, 
#         while, 
#         yield
        
# 2. Data Types:
#     --> each data type: defintion, properties, methods, data engineering
#     --> int, float, string, tuple, list, set, dict
    
# 3. In-built Functions
#     --> Covered
#     --> Open() function:
#     open(file_path, mode)
    
#     "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    
#     Code Snippet:
#     ------------
#     f = open(r"C:\Users\UMESH\Desktop\customersonetwothree.txt", "r")
#     print(f.read())
    
#     Error:
#     FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\UMESH\\Desktop\\customersonetwothree.txt'
    
#     "a" - Append - Opens a file for appending, creates the file if it does not exist
    
#     It creates the new file.
    
#     Code Snippet:
#     --------------
#     f = open(r"C:\Users\UMESH\Desktop\customersonetwothree.txt", "a") 
    
#     "w" - Write - Opens a file for writing, creates the file if it does not exist
    
#     Code Snippet:
#     f = open("demofile3.txt", "a") # in this statement we are using open() in built function to open a file.
#     f.writelines(["\nSee you soon!", "\nOver and out."])
#     f.close() # when you open a file in python. it is to be closed once writing or editing is done with the file.
    
#     #open and read the file after the appending:
#     f = open("demofile3.txt", "r")
#     print(f.read())



# 4. Modules/UDFs/File Handling/Classes

# 5. Operators of Python:
#    Python divides the operators in the following groups:

#     @ Arithmetic operators
#     @ Assignment operators
#     @ Comparison operators:
#       <*> Comparison operators are used to compare two values:

#         Operator	Name	                    Example	 
#         ==	        Equal	                    x == y	
#         !=	        Not equal	                x != y	
#         >	        Greater than	            x > y	
#         <	        Less than	                x < y	
#         >=	        Greater than or equal to	x >= y	
#         <=	        Less than or equal to	    x <= y
        
#     @ Logical operators
#     @ Identity operators
#     @ Membership operators 
#     @ Operator Precedence
    
 
# Python def Keyword:
# --------------------
#     >> Definition and Usage
#         :: The def keyword is used to create, (or define) a function.
        
        
# a block of code:
#     >> collection of stetements
#     >> grouped together
#     >> They should have logical arragment in execution in order to solve the problem
    
# Sample functin Creation:(UDFs/File)
# -----------------------------------
# def my_function():
#   print("Hello from a function") 

# Task: Finding Even Numbers
# def even_numbs_finder():
#     tuple = (1,2,3,4,5)
#     for d in tuple:
#         if d % 2 == 0:
#            print(f"{d} is an even number")
#         else:
#            print(f"{d} is not an even number")
       
       
# Key Points:
# -----------
# @ A function is a block of code which only runs when it is called. In other words, we need to call the functin by it's name in order to the code block of that function.

# A simple function that takes no parameters and returns a greeting.
# def greet():
#     return "Hello, world!"

# print(greet())  # Output: Hello, world!



# 2. Function with Parameters
# A function that takes parameters and returns the result.
# def add_numbers(a, b):
#     return a + b

# print(add_numbers(3, 5))  # Output: 8