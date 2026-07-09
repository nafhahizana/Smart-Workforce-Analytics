import pandas as pd

# Load dataset
data = pd.read_csv("dataset/employees.csv")

print("Original Data")
print(data)


# Remove Employee_ID and Name
data_cleaned = data.drop(["Employee_ID", "Name"], axis=1)


print("\nAfter Removing Unnecessary Columns")
print(data_cleaned)


data_cleaned = pd.get_dummies(data_cleaned, columns=["Department"])


print("\nAfter Encoding Department")
print(data_cleaned)


data_cleaned.to_csv("dataset/cleaned_employees.csv", index=False)


print("\nCleaned dataset saved successfully!")