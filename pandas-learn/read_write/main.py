
import pandas as pd
if __name__ == '__main__':
    data = pd.read_csv("titanic.csv")
    print(data.info())
    print(data.dtypes)
    # data.to_excel("titanic.xlsx",sheet_name="passangers",index=False)
    data.to_excel("titanic.xlsx",sheet_name="passanger_two",index=False)
