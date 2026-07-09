import pandas as pd


# -----------------------------
# Load Datasets
# -----------------------------

attendance = pd.read_csv(
    "dataset/attendance.csv"
)

leave = pd.read_csv(
    "dataset/leave_records.csv"
)

salary = pd.read_csv(
    "dataset/salary.csv"
)


# -----------------------------
# Attendance Analysis
# -----------------------------

attendance_summary = attendance.groupby(
    "Employee_ID"
).agg(

    Total_Days=("Status", "count"),

    Present_Days=(
    "Status",
    lambda x: ((x == "Present") | (x == "Late")).sum()
),

    Absent_Days=(
        "Status",
        lambda x: (x == "Absent").sum()
    ),

    Late_Days=(
        "Status",
        lambda x: (x == "Late").sum()
    ),

    Average_Working_Hours=(
        "Working_Hours",
        "mean"
    )

).reset_index()


# Attendance Percentage

attendance_summary["Attendance_Percentage"] = (

    attendance_summary["Present_Days"]
    /
    attendance_summary["Total_Days"]

) * 100


# -----------------------------
# Leave Analysis
# -----------------------------

leave_summary = leave.groupby(
    "Employee_ID"
).size().reset_index(
    name="Total_Leaves"
)


# Merge Leave Data

attendance_summary = attendance_summary.merge(
    leave_summary,
    on="Employee_ID",
    how="left"
)


attendance_summary["Total_Leaves"] = (
    attendance_summary["Total_Leaves"]
    .fillna(0)
)


# -----------------------------
# Salary Deduction Rule
# -----------------------------

# 1 paid leave allowed per month
# Extra leave = deduction

salary = salary.merge(
    attendance_summary[
        [
            "Employee_ID",
            "Total_Leaves"
        ]
    ],
    on="Employee_ID",
    how="left"
)


salary["Extra_Leave"] = (

    salary["Total_Leaves"] - 1

)


salary["Extra_Leave"] = salary[
    "Extra_Leave"
].apply(
    lambda x: x if x > 0 else 0
)


# Assume one day salary deduction

salary["Deduction"] = (

    salary["Gross_Salary"] / 30

) * salary["Extra_Leave"]


salary["Deduction"] = salary[
    "Deduction"
].round(2)


salary["Net_Salary"] = (

    salary["Gross_Salary"]
    -
    salary["Deduction"]

)


# -----------------------------
# Save Reports
# -----------------------------

attendance_summary.to_csv(
    "exports/attendance_analysis.csv",
    index=False
)


salary.to_csv(
    "exports/salary_analysis.csv",
    index=False
)


print("HR Analysis Completed!")
print("\nAttendance Analysis:")
print(attendance_summary.head())


print("\nSalary Analysis:")
print(salary.head())