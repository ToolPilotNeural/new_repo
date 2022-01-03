import math


def add_two_numbers(a, b) -> int:
    return a + b

def subtract_two_numbers(a, b) -> int:
    return a - b

def multiply_two_numbers(a, b) -> int:
    return a * b

def divide_two_numbers(a, b) -> int:
    try:
        return a/b

    except ZeroDivisionError:
        print('You cannot divide a number by zero')
        return None
