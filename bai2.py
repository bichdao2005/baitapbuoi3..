# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:31:47 2024

@author: Bich Dao
"""

a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
print("tổng", a+b)
print("hiệu",a-b)
print("tích",a*b)
thuong=a/b
laydu=a%b
laynguyen=a//b
print(" thương", round(thuong,3))
print("chia lấy phần nguyên",round(laynguyen,3))
print("chia lấy dư" , round(laydu,3))
