import pandas as pd


# 旧列 -> 转换  -> 新列
def create_new_columns():
    air_quality = pd.read_csv("../data/air_quality_no2.csv", index_col=0, parse_dates=True)
    air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
    print(air_quality[["london_mg_per_cubic", "station_london"]])

    air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
    print(air_quality[["ratio_paris_antwerp","station_paris","station_antwerp"]])


# 修改列名
def re_name():
    air_quality = pd.read_csv("../data/air_quality_no2.csv", index_col=0, parse_dates=True)
    air_quality_renamed = air_quality.rename(
        columns={
            "station_antwerp":"BETR801",
            "station_paris":"FR04014",
            "station_london":"London Westminster",
        }
    )
    print(air_quality_renamed.head())

    air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
    print(air_quality_renamed.head())


if __name__ == '__main__':
    # user_chinese_data = pd.read_csv('user_chinese.csv')
    # print(user_chinese_data)
    # user_english_data = pd.read_csv('user_english.csv')
    # print(user_english_data)
    #
    # concat_data = pd.concat([user_chinese_data, user_english_data],axis=0)
    # print(concat_data)
    user_chinese_data = pd.read_csv('user_chinese.csv')
    order_chinese_data = pd.read_csv('order_chinese.csv')
    merge_data = pd.merge(user_chinese_data,order_chinese_data,how='left',on="user_id")
    print(merge_data)



