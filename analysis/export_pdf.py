import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet


# Load Data

attendance = pd.read_csv(
    "exports/attendance_analysis.csv"
)

salary = pd.read_csv(
    "exports/salary_analysis.csv"
)


# PDF Location

pdf_file = "exports/HR_Analytics_Report.pdf"


doc = SimpleDocTemplate(
    pdf_file
)


styles = getSampleStyleSheet()


content = []


# Title

content.append(
    Paragraph(
        "Smart Workforce Analytics & HR Decision Support System",
        styles["Title"]
    )
)

content.append(
    Spacer(1,20)
)


# Attendance Summary

content.append(
    Paragraph(
        "Attendance Analysis Report",
        styles["Heading2"]
    )
)


attendance_data = [
    [
        "Employee ID",
        "Present Days",
        "Absent Days",
        "Late Days",
        "Attendance %"
    ]
]


for _, row in attendance.head(10).iterrows():

    attendance_data.append(
        [
            str(row["Employee_ID"]),
            str(row["Present_Days"]),
            str(row["Absent_Days"]),
            str(row["Late_Days"]),
            f"{row['Attendance_Percentage']:.2f}%"
        ]
    )


table = Table(attendance_data)


table.setStyle(
    TableStyle(
        [
            ("GRID",(0,0),(-1,-1),0.5,None)
        ]
    )
)


content.append(table)


content.append(
    Spacer(1,20)
)



# Salary Report

content.append(
    Paragraph(
        "Salary Deduction Report",
        styles["Heading2"]
    )
)


salary_data = [
    [
        "Employee ID",
        "Gross Salary",
        "Deduction",
        "Net Salary"
    ]
]


for _, row in salary.head(10).iterrows():

    salary_data.append(
        [
            str(row["Employee_ID"]),
            str(row["Gross_Salary"]),
            str(row["Deduction"]),
            str(row["Net_Salary"])
        ]
    )


table2 = Table(salary_data)


table2.setStyle(
    TableStyle(
        [
            ("GRID",(0,0),(-1,-1),0.5,None)
        ]
    )
)


content.append(table2)



doc.build(content)


print("PDF Report Generated Successfully!")