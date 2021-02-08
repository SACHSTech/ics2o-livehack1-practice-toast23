"""
-------------------------------------------------------------------------------
Name:   minutes_days.py
Purpose:  convert minutes to days, hours, and minutes
 
Author: Yao.T
 
Created:  08/02/2021
------------------------------------------------------------------------------
"""

#get mins
minutes = int(input("Enter minutes"))

#convert to days + hours + mins 
days = minutes / 1440
hours = minutes % 1440 / 60
minsLeft = minutes % 1440 % 60

#output
print(f"\n{int(days)} days, {int(hours)} hours, and {int(minsLeft)} minutes.")

