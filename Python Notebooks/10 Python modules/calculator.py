# Calculator module

"""This the calculator module"""

def add(a,b):
    return a+b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return e
    


# variable inside module

pi = 3.1459
