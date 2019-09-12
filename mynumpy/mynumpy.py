import numpy as np


class mynumpy:
    @staticmethod
    def desc():
        print("这是numpy的一些测试")


if __name__ == '__main__':
    # 生成 数组 [0 1 2 3 4 5]
    arr1 = np.arange(6)

    # 切割 一维数组 为 二维数组 [[0 1 2] [3 4 5]]
    arr2 = arr1.reshape((2, 3))

    # 数组 的算术运算 [[2 3 4] [5 6 7]]
    reshape_arithmetic = arr2 + 2

    # 数组 与 数组 的运算 [[ 0  2  4] [ 6  8 10]]
    arange_reshape = arr2 + arr2
    print(arange_reshape)
