# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:03:01 2024

@author: Bich Dao
"""

a= float(input("nhập vào số a: "))
b= float(input("nhập vào số b: "))
c= float(input("nhập vào số c: "))
if a!=0:
    print("{0}x**2+{1}x+{2}=0".format(a,b,c))
else:
    print("không phải phương trình bậc 2")