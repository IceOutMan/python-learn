import numpy as np
import pandas as pd

if __name__ == '__main__':
    data = {
        'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 50, 300, 250, 30, 100],
        'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Jan', 'Mar']
    }

    df = pd.DataFrame(data)
    print(df.sort_values(by=['Product']))
    print("===================================================")
    pivot_table = df.pivot_table(index='Product', columns='Month', values='Sales', aggfunc='sum')
    print(pivot_table)
