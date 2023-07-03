import matplotlib
from matplotlib  import pyplot as plt

matplotlib.rc("font", family='Songti SC', weight="bold")

if __name__ == '__main__':
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
