#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:35:50 2024

@author: andrewpayne
"""

"""
Change between types
"""
#test = 10
#str_test = str(test)

#print("I am going to put " + str(test))

#str_number = '35.5'
#int_number = float(str_number)

"""
Gathering input from User
"""
"""
Write the code to calculate the sales tax for the province of NL
Given:
    Sale total = 200
    Tax Rate = 15 %
"""

# input()

# =============================================================================
# sale_total = input("Enter the sales total before tax: ")
# sale_total = float(sale_total)
# tax_rate = float(input("Enter the tax rate: ")) / 100
# sales_tax = sale_total * tax_rate
# 
# print("The sales tax of the purchase is: ", end='')
# print(sales_tax, end=' $\n')
# 
# print("The sales tax is: $ {}".format(sales_tax))
# 
# print(f"The sales tax is: $ {sales_tax}")
# =============================================================================

"""
Write the code to calculate the perimeter and area of a rectangle
Given:
    Side a = 10
    Side b = 20
"""

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))

perimeter = (2 * side_a) + (2 * side_b)
area = side_a * side_b

print(f"The perimeter of the rectangle is {perimeter} and area is {area}.")

