import numpy as np


class mynumpy:
    @staticmethod
    def desc():
        print("这是numpy的一些测试")


if __name__ == '__main__':
    arange = np.arange(6)
    # print(arange)
    arange_reshape = arange.reshape((2, 3))
    # print("#########")
    print(arange_reshape)
    reshape_ = arange_reshape + 2
    print("#########")
    print(reshape_)
    arange__reshape = np.arange(6).reshape((2, 3))
    arange_reshape = arange__reshape + arange_reshape
    print("#########")
    print(arange_reshape)
