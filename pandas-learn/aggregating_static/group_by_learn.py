import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame(data={
        'Sex': ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'F', 'F'],
        'Age': [1, 1, 2, 2, 3, 3, 3, 4, 4]
    })
    print(df)
    print(df.groupby('Sex')['Age'].mean())
