# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 02:35:24 2021

@author: PC
"""
import numpy as np

list0 = []
x = 0
for i in range(9):
    num = int(input("Enter number here:"))
    
    list0.append(num)
print(list0)
list1 = np.array(list0)

mean = list1.mean()
variance = list1.var()
stan_dev = list1.std()

print("Mean is %s" %mean)
print("Variance is %f" %variance)
print("Standard deviation is %u" %stan_dev)