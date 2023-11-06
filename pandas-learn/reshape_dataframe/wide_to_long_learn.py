import numpy as np
import pandas as pd

if __name__ == '__main__':
    data = {
        'Student_ID': [1, 2],
        'Math_1': [80, 90],
        'Math_2': [85, 88],
        'Science_1': [75, 78],
        'Science_2': [80, 82]
    }

    df = pd.DataFrame(data)
    print(df)
    print("===============================================")
    long_df = pd.wide_to_long(df, stubnames=['Math', 'Science'],sep='_', i='Student_ID', j='Exam')
    print(long_df)

