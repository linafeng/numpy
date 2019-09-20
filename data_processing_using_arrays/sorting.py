# -*- coding: utf-8 -*-

import numpy.random as np_random

print('一维数组排序')
arr = np_random.randn(3)
arr.sort()
print(arr)
print()

print('二维数组排序')
arr = np_random.randn(3, 2)
print(arr)
arr.sort(1)  # 对每一行元素做排序
print(arr)

print('找位置在5%的数字')
large_arr = np_random.randn(100)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])
