# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 08:52:49 2021

@author: PC
"""

'''Print factorial of a number'''

n = int(input("Enter the number here: "))
product = 1
for i in range(1,n+1):
    product = product*i
    
print(product)