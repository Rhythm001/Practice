# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:05:27 2021

@author: PC
"""

marks=float(input(("Enter your marks here: ")))
max_marks=float(input("Enter the maximum possible marks: "))

perc=(marks/max_marks)*100

if (perc>90 and perc<=100):
    print(perc,"% A Grade. Congratulations!")
elif(perc>80 and perc<=90):
    print(perc,"% B Grade.")
elif(perc>70 and perc<=80):
    print(perc,"% C Grade.")
elif(perc>60 and perc<=70):
    print(perc,"% D Grade")
else:
    print(perc,"% Fail.\nTry again later. You can make it.")
    