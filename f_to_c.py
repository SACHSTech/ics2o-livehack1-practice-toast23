"""
-------------------------------------------------------------------------------
Name:   f_to_c.py
Purpose:  Convert fahrenheit to celsius
 
Author: Yao.T
 
Created:  08/02/2021
------------------------------------------------------------------------------
"""

#get degrees Fahrenheit
degreeF = float(input("Degrees in Fahrenheit: "))

#convert Fahrentheit to Celsius
degreeC = (degreeF-32) / 1.8

#output
print(f"\nDegrees in Celsius: {round(degreeC, 2)}")