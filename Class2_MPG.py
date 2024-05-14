#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 17:14:02 2024

@author: andrewpayne
"""

"""
Get the amount of miles driven and gallons of gas used as inputs.
Data should be stored as a float.
"""
miles_driven = float(input("Enter the amount of miles driven: "))
gas_used = float(input("Enter the amount of gas used: "))

# Perform the calculation based on inputs to provide the MPG.

miles_per_gallon = miles_driven / gas_used

# Display the information to the user

x = ' '

print('\n')
print('The Miles Per Gallon program \n')

print('Enter miles driven:', 13*x, miles_driven)

print('Enter gallons of gas used:', 6*x, gas_used)

print('\nMiles Per Gallon:', 15*x, round(miles_per_gallon,2))

print('\nBye!')




 
 

