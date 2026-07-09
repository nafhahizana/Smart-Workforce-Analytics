import pandas as pd

data = pd.read_csv("dataset/employees.csv")

print("EMPLOYEE DATA")
print("====================")
print(data)

print("\nDataset Shape:")
print(data.shape)

print("\nColumns:")
print(data.columns)

print("\nData Types:")
print(data.dtypes)

print("\nStatistical Summary:")
print(data.describe())