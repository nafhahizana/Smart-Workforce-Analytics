import pandas as pd
import random
from datetime import datetime, timedelta


# -----------------------------
# Employee Master Dataset
# -----------------------------

employees = []

names = [
    "Asha", "Ravi", "Meena", "John", "Priya",
    "Kiran", "Anu", "Rahul", "Divya", "Arun"
]

departments = [
    "IT",
    "HR",
    "Finance",
    "Marketing",
    "Sales"
]

designations = [
    "Developer",
    "Manager",
    "Analyst",
    "Executive",
    "Team Lead"
]


for i in range(1, 101):

    employees.append([
        i,
        random.choice(names) + str(i),
        random.randint(22, 55),
        random.choice(departments),
        random.choice(designations),
        random.randint(30000, 90000)
    ])


employee_df = pd.DataFrame(
    employees,
    columns=[
        "Employee_ID",
        "Employee_Name",
        "Age",
        "Department",
        "Designation",
        "Monthly_Salary"
    ]
)


employee_df.to_csv(
    "dataset/employee_master.csv",
    index=False
)


# -----------------------------
# Attendance Dataset
# -----------------------------

attendance = []

start_date = datetime(2026, 1, 1)


for emp_id in range(1, 101):

    for day in range(90):

        date = start_date + timedelta(days=day)

        login_hour = 9
        login_minute = random.randint(0, 40)

        login_time = datetime(
            2026,
            1,
            1,
            login_hour,
            login_minute
        )


        if login_minute > 15:
            status = "Late"
        else:
            status = "Present"


        if random.random() < 0.05:
            status = "Absent"


        working_hours = round(
            random.uniform(6, 9),
            2
        )


        logout_time = login_time + timedelta(
            hours=working_hours
        )


        attendance.append([
            emp_id,
            date.strftime("%Y-%m-%d"),
            login_time.strftime("%H:%M"),
            logout_time.strftime("%H:%M"),
            status,
            working_hours
        ])


attendance_df = pd.DataFrame(
    attendance,
    columns=[
        "Employee_ID",
        "Date",
        "Login_Time",
        "Logout_Time",
        "Status",
        "Working_Hours"
    ]
)


attendance_df.to_csv(
    "dataset/attendance.csv",
    index=False
)


# -----------------------------
# Leave Dataset
# -----------------------------

leaves = []

leave_types = [
    "Paid Leave",
    "Sick Leave",
    "Casual Leave"
]


for i in range(300):

    leaves.append([
        random.randint(1,100),
        random.choice(leave_types),
        (
            start_date +
            timedelta(days=random.randint(1,90))
        ).strftime("%Y-%m-%d")
    ])


leave_df = pd.DataFrame(
    leaves,
    columns=[
        "Employee_ID",
        "Leave_Type",
        "Leave_Date"
    ]
)


leave_df.to_csv(
    "dataset/leave_records.csv",
    index=False
)


# -----------------------------
# Salary Dataset
# -----------------------------

salary = []


for row in employee_df.itertuples():

    salary.append([
        row.Employee_ID,
        row.Monthly_Salary,
        0,
        row.Monthly_Salary
    ])


salary_df = pd.DataFrame(
    salary,
    columns=[
        "Employee_ID",
        "Gross_Salary",
        "Deduction",
        "Net_Salary"
    ]
)


salary_df.to_csv(
    "dataset/salary.csv",
    index=False
)


print("HR datasets created successfully!")