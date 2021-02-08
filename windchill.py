"""
-------------------------------------------------------------------------------
Name:   windchill.py
Purpose:  computes windchill factor
 
Author: Yao.T
 
Created:  08/02/2021
------------------------------------------------------------------------------
"""

#get temperature(C) and windspeed(km/h)
T = float(input("Enter the temperature in celsius: "))
V = float(input("Enter windspeed (km/h): "))

#calculate windchill factor
windChill = 13.12 + (0.6215*T) - (11.37 * (V**0.16)) + (0.3965 * T * (V**0.16))

#output
print(f"\nWindchill: {round(windChill, 2)}")