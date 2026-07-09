import pandas as pd


# Load Data

attendance = pd.read_csv(
    "exports/attendance_analysis.csv"
)

salary = pd.read_csv(
    "exports/salary_analysis.csv"
)

employees = pd.read_csv(
    "dataset/employee_master.csv"
)



# Create Excel Report

with pd.ExcelWriter(
    "exports/HR_Analytics_Report.xlsx"
) as writer:

    employees.to_excel(
        writer,
        sheet_name="Employee Master",
        index=False
    )

    attendance.to_excel(
        writer,
        sheet_name="Attendance Analysis",
        index=False
    )

    salary.to_excel(
        writer,
        sheet_name="Salary Analysis",
        index=False
    )


print(
    "Excel Report Generated Successfully!"
)