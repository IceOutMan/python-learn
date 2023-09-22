import pandas as pd

if __name__ == '__main__':
    data_frame = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    df = pd.DataFrame(data=data_frame, columns=['A', 'B', 'C','D'])
    print(df)

