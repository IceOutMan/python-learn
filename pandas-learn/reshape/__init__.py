import pandas as pd

def sort_table_rows():
   titanic = pd.read_csv("titanic.csv")
   temp_data = titanic.sort_values(by="Age")
   print(temp_data['Age'])

   temp_data = titanic.sort_values(by=["Pclass","Age"], ascending=False)
   print(temp_data)

def pivot():
   no2 = pd.read_csv('air_quality_long.csv', parse_dates=True)
   # no2 = air_quality[air_quality["parameter"] == "no2"]
   no2_subset = no2.sort_index().groupby(["location"]).head(2) # head() Return first n rows of each group.
   no2_pivoted = no2.pivot(columns="location", values="value")
   print(no2_pivoted)
   # no_2 = no2_pivoted.melt(id_vars="date.utc")
   # print(no_2)

if __name__ == '__main__':
    # sort_table_rows()
    pivot()



