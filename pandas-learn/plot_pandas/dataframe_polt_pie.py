import pandas as pd
import matplotlib.pyplot as plot

if __name__ == '__main__':
    df = pd.DataFrame(
        data={
            'mass': [0.330, 4.87, 5.97],
            'radius': [2439.7, 6051.8, 6378.1]
        },
        index=['Mercury', 'Venus', 'Earth'])

    print(df)
    df.plot.pie(y='radius', figsize=(5, 5))

    plot.show()
