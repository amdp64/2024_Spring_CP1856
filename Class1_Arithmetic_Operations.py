#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:38:00 2024

@author: andrewpayne
"""

"""
Python Arithmetic Operators
+ Addition
- Subtraction
* Multiplication
/ Division 
// Floor (Integer) Division
% Modulus / Modulo / Remainder 
** Exponential (to the power of)
"""

add_example = 7 + 9.5
sub_example = 7 - 9
mul_example = 2 * 3
div_example = 8 / 3
flr_div = 8 // 3
mod_example = 7 % 3
exp_example = 2 ** 3

# print(2 * (7 + 3)) # Semantic error. 

"""
Write the code to calculate the sales tax for the province of NL
Given:
    Sale total = 200
    Tax Rate = 15 %
"""

sale_total = 200
tax_rate = 0.15

# after_tax = pre_tax + (pre_tax * tax_rate)
sales_tax = sale_total * tax_rate
print("The sales tax of the purchase is: ", end='')
print(sales_tax)

"""
Write the code to calculate the perimeter and area of a rectangle
Given:
    Side a = 10
    Side b = 20
"""

side_a = 10
side_b = 20

perimeter = (2 * side_a) + (2 * side_b)
# print("The perimeter of the rectangle is: ", end='')
# print(perimeter)

area = side_a * side_b
# print("The area of the rectangle is: ", end='')
# print(area)

print(f"The perimeter of the rectangle is {perimeter} and area is {area}.")
