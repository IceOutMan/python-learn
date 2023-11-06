import pandas as pd

if __name__ == '__main__':
    data_from_excel = pd.read_excel("../data/temp_read.xlsx", sheet_name="MK")
    print(data_from_excel.head())
    data_from_excel.to_excel("../data/temp_save.xlsx", sheet_name="SAVE_MK", index=False)