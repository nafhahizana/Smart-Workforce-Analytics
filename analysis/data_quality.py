import pandas as pd

data = pd.read_csv("dataset/employees.csv")


print("MISSING VALUES")
print("================")
print(data.isnull().sum())


print("\nDUPLICATE ROWS")
print("================")
print(data.duplicated().sum())


print("\nUNIQUE VALUES")
print("================")
print(data.nunique())