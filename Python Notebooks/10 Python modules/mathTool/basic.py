# basic math.py

"""This basic math module"""

def add(a,b):
    """Addition of two numbers"""
    return a+b

def subtract(a,b):
    """subtraction of two numbers"""
    return a - b

def multiply(a,b):
    """multiplication of two numbers"""
    return a * b

def divide(a,b):
    """division between numbers"""
    try:
        return a/b
    except ZeroDivisionError as e:
        return e
    


