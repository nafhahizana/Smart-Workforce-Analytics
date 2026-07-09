import pandas as pd

data = pd.read_csv("dataset/employees.csv")

print("EMPLOYEE DATA")
print("====================")
print(data)

print("\nTotal Employees:")
print(len(data))

print("\nAverage Salary:")
print(data["Salary"].mean())

print("\nAverage Performance Score:")
print(data["Performance_Score"].mean())