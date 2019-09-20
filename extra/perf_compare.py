import timeit
import numpy

common_for = """
for d in data:
    s += d
"""

common_sum = """
sum(data)
"""

common_numpy_sum = """
numpy.sum(data)
"""


def timeit_list(n, loops):
    list_setup = """
import numpy
data = [1] * {}
s = 0
""".format(n)
    print('list:')
    print(timeit.timeit(common_for, list_setup, number=loops))
    print(timeit.timeit(common_sum, list_setup, number=loops))
    print(timeit.timeit(common_numpy_sum, list_setup, number=loops))


def timeit_array(n, loops):
    array_setup = """
import numpy
import array
data = array.array('L', [1] * {})
s = 0
""".format(n)
    print('array:')
    print(timeit.timeit(common_for, array_setup, number=loops))
    print(timeit.timeit(common_sum, array_setup, number=loops))
    print(timeit.timeit(common_numpy_sum, array_setup, number=loops))


def timeit_numpy(n, loops):
    numpy_setup = """
import numpy
data = numpy.array([1] * {})
s = 0
""".format(n)
    print('numpy:')
    print(timeit.timeit(common_for, numpy_setup, number=loops))
    print(timeit.timeit(common_sum, numpy_setup, number=loops))
    print(timeit.timeit(common_numpy_sum, numpy_setup, number=loops))


if __name__ == '__main__':
    timeit_list(50000, 800)
    timeit_array(50000, 800)
    timeit_numpy(50000, 800)
    # print(numpy.sum(numpy.array([1] * 5))) 结果是5，前面是生成5个1的数组
