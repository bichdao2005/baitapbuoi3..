# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:14:58 2024

@author: Bich Dao
"""
N= int(input("nhập vào số nguyên dương có hai chữ số: "))
if N>=10 and N<=99 :
    print("Tổng các chữ số của N ", N//10+N%10)
else:
    print("không xác định")
