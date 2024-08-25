# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:22:29 2024

@author: Bich Dao
"""
import math
a=float(input("Nhập vào a: "))
b=float(input("Nhập vào b: "))
A=math.sqrt(a)-math.sqrt(b)
B=math.sqrt(math.sqrt(a))- math.sqrt(math.sqrt(b))
C=math.sqrt(a) + math.sqrt(math.sqrt(a*b))
D=math.sqrt(math.sqrt(a))+math.sqrt(math.sqrt(b)) 
print("kết quả là", A/B-C/D)
                    