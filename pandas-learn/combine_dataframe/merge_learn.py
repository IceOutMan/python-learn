import pandas as pd

if __name__ == '__main__':

    user_chinese_data = pd.read_csv('user_chinese.csv')
    order_chinese_data = pd.read_csv('order_chinese.csv')
    merge_data = pd.merge(user_chinese_data,order_chinese_data,how='left',on="user_id")
    print(merge_data)



