import pandas as pd

if __name__ == '__main__':
    data = {
        'a': 11,
        'b': 22,
        'c': 33
    }
    age = pd.Series(data=data, name="Age", index=['a','b','c','d'])
    print(age.min())
    print(age.max())
    print(age.agg(['min','max','sum']))
    print(age.to_frame())
    print(age.keys())
    print(age.isna())
    print(age.isnull())


