import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/employees.csv")


department_count = data["Department"].value_counts()


plt.figure(figsize=(8,5))

plt.bar(department_count.index, department_count.values)

plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employee Distribution by Department")

plt.show()
