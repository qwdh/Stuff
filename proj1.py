
import math

'''
Project: Operation Calculator
by: Jack aka RoboNuts
Date made: 1/25/2022
Date last updated: 1/26/2022
'''

print('Welcome to Jack\'s calculator!')
number_nums = input('How many numbers do you need to calculate? ', )

if number_nums <= '2':
    print('Please enter one of the following:')
    print('+, -, *, /')
    print('sqrt, abs, pow')
    math_type = input()  # asking for the user's desired form of arithmetic
if number_nums > '2':
    print('Please enter one of the following:')
    print('+, -, *, /')
    math_type_many = input()


if math_type == '+': #addition
    x_add = int(input('Enter first value: '))
    y_add = int(input('Enter second value: '))
    z_add = x_add + y_add
    print('Calculating....Done!')
    print('The summation of', x_add, 'and', y_add, 'is: ', z_add)

elif math_type == '-': #subtraction
    x_sub = int(input('Enter first value: '))
    y_sub = int(input('Enter second value: '))
    z_sub = x_sub - y_sub
    print('Calculating....Done!')
    print('The subtraction of', x_sub, 'and', y_sub, 'is: ', z_sub)

elif math_type == '*': #multiplication
    x_mul = int(input('Enter first value: '))
    y_mul = int(input('Enter second value: '))
    z_mul = (x_mul * y_mul)
    print('Calculating....Done!')
    print('The multiplication of', x_mul, 'and', y_mul, 'is', z_mul)

elif math_type == '/': #divison
    x_div = int(input('Enter first value: '))
    y_div = int(input('Enter second value: '))
    z_div = (x_div / y_div)
    print('Calculating....Done!')
    print('The division of', x_div, 'and', y_div, 'is', z_div)

elif math_type == 'sqrt': #square root
    x_sqrt = int(input('Enter an integer: '))
    y_sqrt = math.sqrt(x_sqrt)
    print('The square root of', x_sqrt, 'is', y_sqrt)

elif math_type == 'pow': #raising number to a power
    x_pow = int(input('Enter the first integer: '))
    y_pow = int(input('Enter the second integer: '))
    z_pow = math.pow(x_pow, y_pow)
    print(z_pow)

elif: math_type == 'abs':
    x_abs = int(input('Enter the an integer: '))
    y_abs = math.abs(x_abs)
    print(y_abs)

elif math_type_many == '+':
    x_add_many = int(input('Enter first integer: '))
    y_add_many = int(input('Enter second integer: '))
    z_add_many = int(input('Enter third integer: '))
    w_add_many = x_add_many + y_add_many + z_add_many
    print('The result of the three integers is: ', w_add_many)







print('Thank you for using Jack\'s calculator!') #nice lil see you later end greeting

