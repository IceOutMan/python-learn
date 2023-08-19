from matplotlib import pyplot as plt
import pandas as pd

if __name__ == '__main__':
    # 用行表示数据
    array_data = [["ZS", "LS", "WW"], [12, 13, 14], ["male", "male", "female"]]
    df = pd.DataFrame(data=array_data, index=[1, 2, 3], columns=['Name', 'Age', 'Sex'])
    print(df)

    print()

    print(df.size)



