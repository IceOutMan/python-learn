import matplotlib
from matplotlib  import pyplot as plt

matplotlib.rc("font", family='Songti SC', weight="bold")

# 折线图
def multi_line_plot():
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

def single_line_plot():
    years = [ 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.2, 1075.9, 5957.3]

    # x轴years， y轴gdp
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    # 添加标题
    plt.title("名义GDP")

    # 给y轴加标记
    plt.ylabel("十亿美元")
    # 给x轴替加标记
    plt.xlabel("年份")
    plt.show()


if __name__ == '__main__':
    multi_line_plot()