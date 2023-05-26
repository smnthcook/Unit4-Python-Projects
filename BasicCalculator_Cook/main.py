'''
Basic Calculator
Samantha Cook
5/3/2023
Python II
'''

import operations


repeat = 'y'
while repeat == 'y':
    num1 = float(input('Enter the first number in the operation >> '))
    operation = input('Enter the operation you would like to perform (+, -, *, /) >> ')
    num2 = float(input('Enter the second number in the operation >> '))
    if operation == '+':
        print(num1, '+', num2, '=', operations.add(num1, num2))
    elif operation == '-':
        print(num1, '-', num2, '=', operations.subtract(num1, num2))
    elif operation == '*':
        print(num1, '*', num2, '=', operations.multiply(num1, num2))
    elif operation == '/':
        print(num1, '/', num2, '=', operations.divide(num1, num2))
    else:
        print('Invaild operation!')
    repeat = input('Would you like to perform another operation? (y/n) >> ')
    