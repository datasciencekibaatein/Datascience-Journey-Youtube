"""this the module for calculating the area of shapes"""

from math import pi

def rectangle_area(length,width):
    """Area of rectangle"""
    return length * width


def square_area(edge):
    """Area of edge"""
    return edge*edge


def circle_area(radius):
    """Area of circle"""
    return pi * radius**2