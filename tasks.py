# Create a class with various mathematical operations (at least 5 of them), utilizing a consolidated decorator to enhance method functionalitie.
# Decorator/s must check type of the values passed to class instance methods and at the same time calcualte execution time.

################ suds nesigavo man ########################
# import time

# class MathematicalOperations:

#     def __init__(self) -> None:
#         pass

#         def test_time(func):
#             def wrapper(*args, **kwargs):
#                 start_time = time.time()
#                 result = func(*args, **kwargs)
#                 end_time = time.time()
#                 print(f"Execution time: {end_time - start_time}")
#                 return result
#             return wrapper
        
#         def calculator(func):
#             def wrapper(*args, **kwargs):
                
#                 result = func(*args, **kwargs)
                
#                 print(f"Resultat: {}")
#                 return result
#             return wrapper        
        
    
#     @test_time
#     def add(self, a, b):
#         return a + b
    
#     @test_time
#     def subtract(self, a, b):
#         return a - b
    
#     @test_time
#     def multiply(self, a, b):
#         return a * b
    
#     @test_time
#     def divide(self, a, b):
#         return a / b
    
#     @test_time
#     def modulo(self, a, b):
#         return a % b
    


# res = add(5, 2)
# print(res)
# #####################################

# import time
# from functools import wraps

# def check_input_type(func):
#     @wraps(func)
#     def wrapper(self, *args, **kwargs):
#         for arg in args:
#             if not isinstance(arg, (int, float)):
#                 raise ValueError("Input must be of type int or float")
#         return func(self, *args, **kwargs)
#     return wrapper

# def calculate_execution_time(func):
#     @wraps(func)
#     def wrapper(self, *args, **kwargs):
#         start_time = time.time()
#         result = func(self, *args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#         return result
#     return wrapper

# class MathOperations:
    
#     @check_input_type
#     @calculate_execution_time
#     def add(self, a, b):
#         return a + b
    
#     @check_input_type
#     @calculate_execution_time
#     def subtract(self, a, b):
#         return a - b
    
#     @check_input_type
#     @calculate_execution_time
#     def multiply(self, a, b):
#         return a * b
    
#     @check_input_type
#     @calculate_execution_time
#     def divide(self, a, b):
#         if b == 0:
#             raise ValueError("Division by zero is not allowed")
#         return a / b
    
#     @check_input_type
#     @calculate_execution_time
#     def power(self, a, b):
#         return a ** b

# # Example usage
# calculator = MathOperations()
# print(calculator.add(5, 3))
# print(calculator.subtract(10, 4))
# print(calculator.multiply(2.5, 4))
# print(calculator.divide(8, 2))
# print(calculator.power(2, 3))  

# ################## Alberto #############################

# from typing import Callable
# import time


# def checker(fn: Callable):
#     def wrapper(self, *args, **kwargs):
#         start_time = time.time()
#         if all(isinstance(i, (int, float)) for i in args):
#             my_func = fn(self, *args, **kwargs)
#         else:
#             print("--- %s seconds ---" % (time.time() - start_time))
#             raise TypeError("Entered values is not numbers")
#         print("--- %s seconds ---" % (time.time() - start_time))
#         return my_func

#     return wrapper


# class Calculator:
#     @checker
#     def addition(self, a: float, b: float) -> float:
#         try:
#             return a + b
#         except Exception as err:
#             print(err)

#     @checker
#     def substraction(self, a: float, b: float) -> float:
#         return a - b

#     @checker
#     def multiplication(self, a: float, b: float) -> float:
#         return a * b

#     @checker
#     def division(self, a: float, b: float) -> float:
#         return a / b

#     @checker
#     def raise_power(self, a: float, b: float) -> float:
#         try:
#             return pow(a, b)
#         except Exception as err:
#             print(err)


# calc = Calculator()

# print(calc.raise_power(21, 51))

###############################################################################################################################
# Create a decorator factory that would slow the execution speed of the decorated function (lets call it delay decorator.).
# Log the execution times to the file.

################ suds nesigavo man ########################
# from typing import Callable

# def do_som(function: Callable) -> Callable:
#     def delay_decorator(fn: Callable):
#         def wrapper(*args, **kwargs):
#             my_func = fn(*args, **kwargs)
#             return function(my_func)
#         return wrapper
#     return delay_decorator

# @do_som(function=slow)
# def slow(a: int, b: int) -> int:
#     return a + b

# print(sum_numbers(1, 2))

# ############################# Alberto ############################

# import logging
# import time
# from typing import Callable

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="time_logger.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     datefmt="%d/%m/%Y %H:%M:%S",
# )


# def delayer(delay_time):
#     def timer(fn: Callable):
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             time.sleep(delay_time)
#             my_func = fn(*args, **kwargs)
#             logging.info("Execution time: %s seconds" % (time.time() - start_time))
#             return my_func

#         return wrapper

#     return timer


# @delayer(1)
# def raise_power(a: int, b: int) -> int:
#     return pow(a, b)


# print(raise_power(5, 5))


# Create a Database management class that would setup all connections and implement CRUD opearations (inside class/classses). 
# There should be a decorator that would handle possible errors. 
# Please check what error hanling class SQLAlchemy provides.
