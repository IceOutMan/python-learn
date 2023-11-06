import pandas as pd


#  通过 dict 构造 DataFrame
#       KEYS作为columns的名称
#       VALUES作为columns的值
#       index 默认递增
def build_data_frame_by_dict():
    data_frame = {
        "Name": ["ZS", "LS", "WW"],
        "Age": [12, 13, 14],
        "Sex": ["male", "male", "female"]
    }
    df = pd.DataFrame(data=data_frame)
    print(df)


# 通过 list 构造 DataFrame
#   list 中的每一个 item 作为 ROW
#   columns 名字默认从 0
#   index 默认从0递增
def build_data_frame_by_series():
    array_data = [
        ["ZS", "LS", "WW"],
        [12, 13, 14],
        ["male", "male", "female"]
    ]
    dataFrame = pd.DataFrame(data=array_data, index=[1, 2, 3], columns=['Name', 'Age', 'Sex'])
    print(dataFrame)


if __name__ == '__main__':
    # build_data_frame_by_series()
    # build_data_frame_by_dict()

    data_frame = {
        "Name": ["ZS", "LS", "WW"],
        "Age": [12, 13, 14],
        "Sex": ["male", "male", "female"]
    }
    df = pd.DataFrame(data=data_frame,index=['a','b','c'])

    print(df)
    df.insert(1, 'Score', [101, 102, 102])
    print(df)



