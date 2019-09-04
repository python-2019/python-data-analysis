from matplotlib import font_manager, pyplot as plt
import numpy as np

class MyMatplotlib:
    """
    mymatplotlib 的一些测试方法
    """

    @staticmethod
    def desc():
        print("mymatplotlib 的一些测试方法")

    @staticmethod
    def plt_weather():
        """
        <<折线图>>
        一天的天气变化
        y:天气参数
        x:时间
        """
        # 设置字体解决中文无法显示的问题
        my_font = font_manager.FontProperties(fname="./font/simsun.ttc")
        # 设置大小和 dpi
        plt.figure(figsize=(20, 8), dpi=80)

        # 时间
        x = range(2, 26, 2)
        # 天气
        y = [11, 13, 15, 17, 19, 20, 23, 34, 32, 32, 30, 18]

        # 画图   # 绘制网格
        plt.plot(x, y, label="温度走势", color="red", linestyle=':', alpha=0.5)

        # 设置x刻度(不设置会根据相应的轴 自动设置)
        # plt.xticks(x)
        # 设置X刻度 绑定对应的字符串或者自定义的刻度 rotation 旋转度数
        plt.xticks(x, ["时间:{}".format(i) for i in x], rotation=0, fontproperties=my_font)

        # 设置y刻度(不设置会根据相应的轴 自动设置)
        plt.yticks(range(-30, 50, 5))

        # 绘制网格
        plt.grid(alpha=0.4, linestyle=":")
        # 设置图例
        plt.legend(loc=0, prop=my_font)
        # 添加描述信息
        # 设置title
        plt.title("0-24点 时间/温度变化曲线图", fontproperties=my_font)
        # 设置 X 描述
        plt.xlabel("时间(单位:小时)", fontproperties=my_font)
        # 设置y描述
        plt.ylabel("温度(单位:摄氏度)", fontproperties=my_font)

        # 保存图片
        plt.savefig("./img/weather.png")
        # show
        plt.show()

    @staticmethod
    def weather_scatter():
        # 利用 numpy 生成 随机数组
        x = np.random.rand(1000)
        y = np.random.rand(1000)
        # 设置 散点图
        plt.scatter(x, y)

        # 保存图片
        plt.savefig("./img/scatter.png")
        # show
        plt.show()


if __name__ == '__main__':
    # MyMatplotlib.plt_weather()
    MyMatplotlib.weather_scatter()
