
import pandas as pd

if __name__ == '__main__':
    titanic = pd.read_csv("../data/titanic.csv")
    adult_names = titanic.iloc[1:2, 2:3]
    print(adult_names)