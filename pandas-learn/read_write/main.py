
import pandas as pd
if __name__ == '__main__':
    df = pd.DataFrame(
        {
            'age': [11, 12, 13],
            'name': ['zs', 'ls', 'ww'],
            'revenue': [111, 222, 333]
        },
        index=['A', 'B', 'C']
    )

    print(df.ge(12))
