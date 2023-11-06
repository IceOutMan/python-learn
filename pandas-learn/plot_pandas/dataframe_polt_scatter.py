import pandas as pd
import matplotlib.pyplot as plot

if __name__ == '__main__':
    df = pd.DataFrame([
        [5.1, 3.5, 0],
        [4.9, 3.0, 0],
        [7.0, 3.2, 1],
        [6.4, 3.2, 1],
        [5.9, 3.0, 2]
    ],columns=['length', 'width', 'species'])
    df.plot.scatter(x='length', y='width',c='DarkBlue')
    plot.show()