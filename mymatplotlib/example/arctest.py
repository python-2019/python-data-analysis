import matplotlib.pyplot as plt
import numpy as np

# https://www.matplotlib.org.cn/gallery/lines_bars_and_markers/bar_stacked.html
def f(t):
    'A damped exponential'
    s1 = np.cos(2 * np.pi * t)
    e1 = np.exp(-t)
    result = s1 * e1
    print(result)
    return result


if __name__ == '__main__':
    #  拉弧测试
    t1 = np.arange(0.0, 5.0, .2)

    l = plt.plot(t1, f(t1), 'ro')
    plt.setp(l, markersize=30)
    plt.setp(l, markerfacecolor='C0')

    plt.show()
