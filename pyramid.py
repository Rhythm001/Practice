# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 08:03:02 2021

@author: PC
"""

'''Write a program to ask user for the number of rows in a pyramid and
print the pyramid of numbers. E.g if the no of rows is 5, then Pyramid
will look like:
1
12
123
1234
12345'''

n = int(input("Enter the number here: "))
for i in range(1, n+1):
    for j in range(i):
        print(j+1, end='')
    print()