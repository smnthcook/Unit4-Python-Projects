'''
Does basic calculation operations.
'''

def add(num1, num2):
    '''
    Returns the sum of the numbers
    '''
    return num1 + num2

def subtract(num1, num2):
    '''
    Returns the sum of the numbers
    '''
    return num1 - num2

def multiply(num1, num2):
    '''
    Return the product of the numbers.
    '''
    return num1 * num2

def divide(num1, num2):
    '''
    Return the quotient of the numbers.
    '''
    if num2 == 0:
        return "Not a number."
    else:
        return num1 / num2
