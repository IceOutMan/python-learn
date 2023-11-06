import pandas as pd

if __name__ == '__main__':
    user_chinese_data = pd.read_csv('user_chinese.csv')
    print(user_chinese_data)
    user_english_data = pd.read_csv('user_english.csv')
    print(user_english_data)

    concat_data = pd.concat([user_chinese_data, user_english_data],axis=0)
    print(concat_data)




