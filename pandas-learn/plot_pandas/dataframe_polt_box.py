import pandas as pd
import matplotlib.pyplot as plot


if __name__ == '__main__':
    age_list = [8, 10, 12, 14, 72, 74, 76, 78, 20, 25, 30, 35, 60, 85]
    df = pd.DataFrame({"gender": list("MMMTMMMMFFTFFF"), "age": age_list})
    ax = df.plot.box(column="age",by='gender', figsize=(10, 8))
    plot.show()