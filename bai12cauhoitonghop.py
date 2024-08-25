# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:13:45 2024

@author: Bich Dao
"""

import random

def main():
    min_value = float(input("Nhập giá trị nhỏ nhất của đoạn: "))
    max_value = float(input("Nhập giá trị lớn nhất của đoạn: "))

    random_number = random.uniform(min_value, max_value)

    print(f"Số ngẫu nhiên trong đoạn [{min_value}, {max_value}] là: {random_number:.2f}")
main()
