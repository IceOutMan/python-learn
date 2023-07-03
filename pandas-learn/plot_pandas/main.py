import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # air_quality = pd.read_csv('air_quality_no2.csv',parse_dates=True,index_col=0)
    # # air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
    # air_quality_renamed = air_quality.rename(
    #     columns={
    #         "station_antwerp": "BETR801",
    #         "station_paris": "FR04014",
    #         "station_london": "London Westminster",
    #     }
    # )
    # air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
    # print(air_quality_renamed.head())
    np.random.seed(1234)
    df = pd.DataFrame(np.random.randn(10, 4),
                      columns=['Col1', 'Col2', 'Col3', 'Col4'])
    print(df)
    boxplot = df.boxplot(column=['Col1', 'Col2', 'Col3'])
    plt.show()
