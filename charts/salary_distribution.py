import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/employees.csv")

plt.figure(figsize=(8,5))

plt.bar(data["Name"], data["Salary"])

plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Salary Distribution")

plt.show()