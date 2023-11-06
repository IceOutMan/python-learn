import pandas as pd

def build_series_by_arr():
    age = pd.Series(data=[11, 22, 33], index=['a', 'b', 'c'], name='Age')
    print(age)

def build_series_by_dict():
    data = {
        'a': 11,
        'b': 22,
        'c': 33
    }
    age = pd.Series(data=data, name="Age")
    print(age)


if __name__ == '__main__':
    data = {
        'a': 11,
        'b': 22,
        'c': 33
    }
    age = pd.Series(data=data, name="Age", index=['a','b','c','d'])
    print(age.index)
    print(age.values)
    print(age.dtypes)
    print(age.name)
    print(age.size)
    print(age.shape)
