
import pandas as pd
if __name__ == '__main__':
    csv_data = pd.read_csv("../data/temp_read.csv")
    print(csv_data.head())
    csv_data.to_csv('../data/temp_save.csv',index=False)
