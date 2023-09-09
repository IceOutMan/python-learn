
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rc("font", family='Songti SC', weight="bold")

def with_label_dot_plot():
    friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h','i']

    plt.scatter(friends, minutes)
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        # 给每个点加标记
        plt.annotate(label,
                     xy=(friend_count,minute_count), # 标记放在对应的点上
                     xytext=(5,-5),                  # 轻微偏离
                     textcoords = 'offset points')

    plt.title("日分钟与朋友数")
    plt.xlabel("朋友数")
    plt.ylabel("花在网站上的日分钟数")
    plt.show()

def base_dot_plot():
    test_1_grades = [ 99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70 ]

    plt.scatter(test_1_grades, test_2_grades)
    plt.title("Axes Aren't Comparable")
    plt.xlabel("测验1的分数")
    plt.ylabel("测试2的分数")
    plt.show()

if __name__ == '__main__':
    # with_label_dot_plot()
    base_dot_plot()

