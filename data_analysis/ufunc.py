# -*- coding: utf-8 -*-
import numpy as np

# 连续数组创建

x1 = np.arange(2, 12, 2)  # 小于stop (start,stop,step)
x2 = np.linspace(1, 9, 5)

print(x1)
print(x2)
# 加减乘除
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))

# 统计函数
# 最大最小

print("最大最小")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(a))
print(np.amin(a, 0))
print(np.amin(a, 1))

print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))

# 统计最大和最小的差值
print("统计最大和最小的差值")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.ptp(a))
print(np.ptp(a, 0))
print(np.ptp(a, 1))

# 统计数组的百分位
print("统计数组的百分位")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))

# 统计数组中的中位数 median()、平均数 mean()
print("统计数组中的中位数 median()、平均数 mean()")
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

# 统计数组中的加权平均值 average()
print("统计数组中的加权平均值 average()")
a = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(a))
print(np.average(a, weights=wts))

# 统计数组中的标准差 std()、方差 var()
print("统计数组中的标准差 std()、方差 var()")
a = np.array([1, 2, 3, 4])
print(np.std(a))
print(np.var(a))

# 排序
print("排序")
a = np.array([[4, 3, 2], [2, 4, 1]])
print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))
