# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:07:21 2021

@author: PC
"""

quantity=int(input("Enter the quantity(in units) here: "))
costperunit=int(input("Enter the cost of 1 unit: "))

cost=quantity*costperunit

discount=(quantity*costperunit)/10 #since it's cost*(10/100)
final=cost-discount

if(cost>1000):
    print("Congrats! You got a discount of %d. You just have to pay %u." %(discount, final))
else:
    print("You have to pay: %f" %cost)
print("Goodbye!")
