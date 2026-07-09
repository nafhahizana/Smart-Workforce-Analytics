import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/employees.csv")


plt.figure(figsize=(8,5))

plt.bar(data["Name"], data["Performance_Score"])

plt.xlabel("Employee Name")
plt.ylabel("Performance Score")
plt.title("Employee Performance Analysis")

plt.ylim(0,10)

plt.show()
