import pandas as pd


# Load datasets

employee = pd.read_csv(
    "dataset/employee_master.csv"
)

attendance = pd.read_csv(
    "dataset/attendance.csv"
)

leave = pd.read_csv(
    "dataset/leave_records.csv"
)

salary = pd.read_csv(
    "dataset/salary.csv"
)


# Remove duplicate rows

employee = employee.drop_duplicates()

attendance = attendance.drop_duplicates()

leave = leave.drop_duplicates()

salary = salary.drop_duplicates()


# Handle missing values

employee = employee.fillna("Unknown")

attendance = attendance.fillna("Unknown")

leave = leave.fillna("Unknown")

salary = salary.fillna(0)


# Save cleaned datasets

employee.to_csv(
    "dataset/clean_employee_master.csv",
    index=False
)

attendance.to_csv(
    "dataset/clean_attendance.csv",
    index=False
)

leave.to_csv(
    "dataset/clean_leave_records.csv",
    index=False
)

salary.to_csv(
    "dataset/clean_salary.csv",
    index=False
)


print("Data Cleaning Completed Successfully!")