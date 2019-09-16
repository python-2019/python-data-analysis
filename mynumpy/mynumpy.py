import numpy as np


class mynumpy:
    @staticmethod
    def desc():
        print("这是numpy的一些测试")

    @staticmethod
    def base1():
        # 生成 数组 [0 1 2 3 4 5]
        arr1 = np.arange(6)

        # 切割 一维数组 为 二维数组 [[0 1 2] [3 4 5]]
        arr2 = arr1.reshape((2, 3))

        # 数组 的算术运算 [[2 3 4] [5 6 7]]
        reshape_arithmetic = arr2 + 2

        # 数组 与 数组 的运算 [[ 0  2  4] [ 6  8 10]]
        arange_reshape = arr2 + arr2


def base2():
    # 创建一维数组 [0 1 2 3 4 5 6 7 8 9]
    arr = np.arange(10)

    # 创建一个布尔数组 [ True  True  True]
    bool_arr = np.full(3, True, dtype=bool)

    # 如何从一维数组中提取满足指定条件的元素？ [1 3 5 7 9]
    filter_arr = arr[arr % 2 == 1]

    # 将arr中的所有奇数替换为 - 1，而不改变arr。 [ 0 -1  2 -1  4 -1  6 -1  8 -1]
    out = np.where(arr % 2 == 1, -1, arr)

    # 将一维数组转换为2行的2维数组 [[0 1 2 3 4] [5 6 7 8 9]]
    arr_reshape = arr.reshape(2, 5)

    # 如何垂直叠加两个数组 [[0 1 2 3 4]  [5 6 7 8 9]]
    a = np.arange(10).reshape(2, -1)

    # repeat 创建重复数组 [[1 1 1 1 1]  [1 1 1 1 1]]
    b = np.repeat(1, 10).reshape(2, -1)

    # concatenate 数组拼接 [[0 1 2 3 4 1 1 1 1 1] [5 6 7 8 9 1 1 1 1 1]]
    concatenate = np.concatenate([a, b], axis=1)

    # 如何获取两个numpy数组之间的公共项？ [2 4]
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    # intersect1d 两个数组的交集
    d = np.intersect1d(a, b)
    # 如何从一个数组中删除存在于另一个数组中的项 [1 2 3 4]
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 6, 7, 8, 9])
    # From 'a' remove all of 'b'
    setdiff_d = np.setdiff1d(a, b)

    #  如何得到两个数组元素匹配的位置 array([1, 3, 5, 7]),)
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

    # where 满足条件(condition)，输出x，不满足输出y。
    # 只有条件 (condition)，没有x和y，则输出满足条件 (即非0) 元素的坐标
    # 结果 [4 4 5 6]
    where = np.where(a == b)
    a[np.where(a > 3)]


def base3():
    # 如何反转二维数组的行？
    arr = np.arange(9)
    # np.array[起點;終點:步長]
    # 如果起點和終點沒有給值，起點自動設為最小值，終點自動設為最大值，
    # 所以np.arange(1, 10, 1)[:]和np.arange(1, 10, 1)[0:9]輸出相同。
    # 因為步長是-1，所以np.arange(1, 10, 1)[::-1]等於np.arange(1, 10, 1)[[-1,-2,-3,-4,-5,-6,-7,-8,-9]]，因此出現反轉。
    # 结果 [8 7 6 5 4 3 2 1 0]
    arr_ = arr[::-1]
    #     如何计算numpy数组的均值，中位数，标准差
    # Input
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')
    sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
    # Solution
    mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
    print(mu, med, sd)


if __name__ == '__main__':
    # 更改数组的形状
    a = np.floor(10 * np.random.random((3, 4)))
    print(a)
