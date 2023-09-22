import numpy as np
import pandas as pd

if __name__ == '__main__':
    data = {
        'city': ['NYC', 'NYC', 'LA', 'LA', 'Chicago', 'Chicago','Chicago'],
        'weather_param': ['temperature', 'humidity', 'temperature', 'humidity', 'temperature', 'humidity','age'],
        'value': [75, 50, 80, 60, 70, 55,99]
    }

    df = pd.DataFrame(data)

    print(df)
    print("===============================================")

    pivot_df = df.pivot(index='city', columns='weather_param', values='value')
    print(pivot_df)
