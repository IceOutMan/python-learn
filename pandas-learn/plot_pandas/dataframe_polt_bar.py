import pandas as pd
import matplotlib.pyplot as plot

if __name__ == '__main__':
    df = pd.DataFrame({
        'sales': [3, 2, 3, 9, 10, 6],
        'signups': [5, 5, 6, 12, 14, 13],
        'visits': [20, 42, 28, 62, 81, 50],
    }, index=pd.date_range(start='2018/01/01', end='2018/07/01', freq='M'))
    print(df)

    df.plot.bar( stacked=True,color={'sales':'red','signups':'green','visits':'blue'})
    plot.show()