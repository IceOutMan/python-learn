import pandas as pd
# 列平均值
def mean():
    titanic = pd.read_csv("../data/titanic.csv")
    print(titanic["Age"].mean())

def median():
    titanic = pd.read_csv("../data/titanic.csv")
    print(titanic[["Age","Fare"]].median())

def describe():
    titanic = pd.read_csv("../data/titanic.csv")
    print(titanic.describe())

# 聚合函数
def agg():
    titanic = pd.read_csv("../data/titanic.csv")
    print(titanic.agg({
        "Age":["min", "max","median","skew"],
        "Fare":["min","max","median","mean"]
    }))

def group_by():
    titanic = pd.read_csv("../data/titanic.csv")
    print(titanic[["Sex","Age"]].groupby(by="Sex").mean())


if __name__ == '__main__':
    mean()
    print("\n")
    median()
    print("\n")
    agg()
    print("\n")
    describe()
    print("\n")
    group_by()


