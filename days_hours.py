"""
-------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  convert hours to days and hours
 
Author: Yao.T
 
Created:  08/02/2021
------------------------------------------------------------------------------
"""

#get hours
hours = int(input("Enter hours: "))

#convert to days + hours and output 
print(f"{int(hours / 24)} days and {hours % 24} hours")

