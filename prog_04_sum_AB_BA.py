# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 10:40:04 2023

@author: master
"""

#input paet a < b 
a = int(input('Enter A = '))
b = int(input('Enter B = '))
#loop
#Init. Loop
sumAB = 0
c = a

#loop body
while (c <= b):
    sumAB = sumAB + c
    c = c + 1  
    #print(c,sumAB)  #for check
    
#output 
print(f'sum form:{a:^5} to {b:^5} is {sumAB:^5}')