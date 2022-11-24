import numpy as np
import pandas as pd

if __name__ == '__main__':
    # city_info_data = pd.read_csv('city_info.csv')
    # pivot_data = city_info_data.pivot(columns='city_name',values='some_value')
    # print(pivot_data)
    # pivot_data = city_info_data.pivot(index='people_category',columns='city_name',values='some_value')
    # print(pivot_data)
    # pivot_table_data = pd.pivot_table(city_info_data, index='people_category',columns='city_name',values='some_value',aggfunc={'some_value':[np.sum,np.mean]})
    # print(pivot_table_data)
    wide_to_long_city_info_data = pd.read_csv('wide_to_long_city_info.csv')
    print(wide_to_long_city_info_data)
    wide_to_long_city_info_data = pd.wide_to_long(wide_to_long_city_info_data,stubnames=['A'],i=['people_category'],j='year')
    print(wide_to_long_city_info_data)



