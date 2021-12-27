from matplotlib import pyplot as plt
import matplotlib

from matplotlib.font_manager import FontManager
import subprocess



def second_line_pic():
    matplotlib.rc("font", family='Songti SC', weight="bold")
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x+y for x,y in zip(variance,bias_squared)]
    print(total_error)
    xs = [i for i,_ in enumerate(variance)]

    # 可以多次调用 plt.plot ，以便在同一个图上显示多个序列
    plt.plot(xs, variance, 'g-', label="variance") # 绿色实线
    plt.plot(xs, bias_squared, 'r-.', label="bias^2") # 红色点虚线
    plt.plot(xs, total_error, 'b:', label="total error") # 蓝色点线

    # 因为已经对每个序列都指派了标记，所以可以自由地布置图例, loc=9，指的是"顶部中央"
    plt.legend(loc=9)
    plt.xlabel("模型复杂度")
    plt.title("偏差-方差权衡图")

    plt.show()




def line_pic():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 1458.3]

    matplotlib.rc("font", family='Songti SC', weight="bold")

    # 创建一幅线图，x轴是年份，y轴是gdp
    plt.plot(years, gdp, color='green', linestyle='solid')

    # 添加一个标题
    plt.title("名义GDP")

    # 给Y轴加标记
    plt.ylabel("十亿美元")
    plt.show()


def bar_pic():
    # grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    # decile = lambda grade: grade // 10 * 10
    matplotlib.rc("font", family='Songti SC', weight="bold")
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    # 条形的默认宽度是 0.8, 因此我们对左侧坐标加上0.1
    # 这样每个条形就被放置在中心了
    xs = [ i+0.1 for i,_ in enumerate(movies)]
    print(xs)

    # 使用左侧X坐标[XS] 和 高度 [num_oscars] 画条形图
    plt.bar(xs, num_oscars)

    plt.ylabel("所获得奥斯卡金像奖数量")
    plt.title("我最喜欢的电影")

    # 使用电影的名字标记x轴，位置在x轴上条形的中心
    plt.xticks(xs, movies)
    plt.show()




if __name__ == '__main__':
    # line_pic()
    # bar_pic()
    second_line_pic()



