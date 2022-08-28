import pandas as pd
if __name__ == '__main__':
    titanic = pd.read_csv("titanic.csv")
    print(titanic["Pclass"].value_counts())


