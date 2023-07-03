from collections import Counter

import matplotlib
from matplotlib import pyplot as plt

matplotlib.rc("font", family='Songti SC', weight="bold")

# 柱状图
def base_bar_pic_plot():
    # grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    # decile = lambda grade: grade // 10 * 10
    matplotlib.rc("font", family='Songti SC', weight="bold")
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    # 条形的默认宽度是 0.8
    xs = [i for i, _ in enumerate(movies)]
    print(xs)

    # x坐标 xs
    # 高度 num_oscars 画条形图
    plt.bar(xs, num_oscars)

    # 使用电影的名字标记x轴，位置在x轴上条形的中心
    plt.xticks(xs, movies)

    # y轴标记
    plt.ylabel("所获得奥斯卡金像奖数量")

    # 标题
    plt.title("我最喜欢的电影")


    plt.show()


def custom_bar_plot():
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    # // 整除
    decile = lambda grade: grade // 10 * 10;
    histogram = Counter(decile(grade) for grade in grades)
    print(histogram)

    # 每个条形向左侧移动4个单位
    # 给每个条形设置正确的高度
    # 每个条形的宽度设置为8
    plt.bar([x-4 for x in histogram.keys()], histogram.values(), 8)

    plt.show()


def test_bar_plot():
    key = [10,20,30]
    val = [1,2,3]
    plt.bar(key, val,8)
    plt.show()

if __name__ == '__main__':
    # base_bar_pic_plot()
    # custom_bar_plot()
    # test_bar_plot()
    base_bar_pic_plot()
