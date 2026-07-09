import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Page Configuration

st.set_page_config(
    page_title="Smart Workforce Analytics",
    layout="wide"
)


st.title("Smart Workforce Analytics & HR Decision Support System")


# -----------------------------
# Load Data
# -----------------------------

employees = pd.read_csv(
    "dataset/employee_master.csv"
)

attendance = pd.read_csv(
    "exports/attendance_analysis.csv"
)

attendance_daily = pd.read_csv(
    "dataset/attendance.csv"
)

leave = pd.read_csv(
    "dataset/leave_records.csv"
)

salary = pd.read_csv(
    "exports/salary_analysis.csv"
)



# -----------------------------
# KPI Section
# -----------------------------

st.subheader("Workforce Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Employees",
        len(employees)
    )


with col2:
    st.metric(
        "Average Attendance %",
        f"{attendance['Attendance_Percentage'].mean():.2f}%"
    )


with col3:
    today = attendance_daily["Date"].max()

    present_today = attendance_daily[
        (attendance_daily["Date"] == today) &
        (
            attendance_daily["Status"].isin(
                ["Present", "Late"]
            )
        )
    ].shape[0]

    st.metric(
        "Present Today",
        present_today
    )


with col4:
    absent_today = attendance_daily[
        (attendance_daily["Date"] == today) &
        (attendance_daily["Status"] == "Absent")
    ].shape[0]

    st.metric(
        "Absent Today",
        absent_today
    )



col5, col6, col7, col8 = st.columns(4)


with col5:
    st.metric(
        "Total Late Arrivals",
        attendance_daily[
            attendance_daily["Status"] == "Late"
        ].shape[0]
    )


with col6:
    st.metric(
        "Average Working Hours",
        f"{attendance['Average_Working_Hours'].mean():.2f}"
    )


with col7:
    paid_leave = leave[
        leave["Leave_Type"] == "Paid Leave"
    ].shape[0]

    st.metric(
        "Paid Leave Usage",
        paid_leave
    )


with col8:
    st.metric(
        "Total Salary Deduction",
        f"₹{salary['Deduction'].sum():,.0f}"
    )



# -----------------------------
# Employee Data
# -----------------------------

st.subheader("Employee Details")

st.dataframe(
    employees
)



# -----------------------------
# Attendance Analysis
# -----------------------------

st.subheader("Attendance Percentage")


fig, ax = plt.subplots(figsize=(10,4))


top_attendance = attendance.head(20)


ax.bar(
    top_attendance["Employee_ID"].astype(str),
    top_attendance["Attendance_Percentage"]
)


ax.set_xlabel("Employee ID")
ax.set_ylabel("Attendance %")
ax.set_title("Employee Attendance Percentage")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Attendance Trend Analysis
# -----------------------------

st.subheader("Daily Attendance Trend")


attendance_daily["Date"] = pd.to_datetime(
    attendance_daily["Date"]
)


daily_attendance = attendance_daily.groupby(
    "Date"
)["Status"].apply(
    lambda x: x.isin(["Present", "Late"]).sum()
)


fig, ax = plt.subplots(figsize=(10,4))


ax.plot(
    daily_attendance.index,
    daily_attendance.values,
    marker="o"
)


ax.set_xlabel("Date")
ax.set_ylabel("Present Employees")
ax.set_title("Daily Attendance Trend")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Monthly Attendance Trend
# -----------------------------

st.subheader("Monthly Attendance Trend")


attendance_daily["Month"] = (
    attendance_daily["Date"]
    .dt.month_name()
)


monthly_attendance = attendance_daily.groupby(
    "Month"
)["Status"].apply(
    lambda x: x.isin(["Present", "Late"]).mean()*100
)

month_order = [
    "January",
    "February",
    "March"
]

monthly_attendance = monthly_attendance.reindex(month_order)


fig, ax = plt.subplots(figsize=(8,4))


ax.bar(
    monthly_attendance.index,
    monthly_attendance.values
)


ax.set_xlabel("Month")
ax.set_ylabel("Attendance Percentage")
ax.set_title("Monthly Attendance Trend")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Employee Performance Analysis
# -----------------------------

st.subheader("Employee Performance Analysis")


performance = attendance.copy()


performance["Performance_Score"] = (
    (performance["Attendance_Percentage"] * 0.6)
    +
    ((performance["Average_Working_Hours"] / 8) * 100 * 0.3)
    -
    (performance["Late_Days"] * 0.1)
)


performance = performance.sort_values(
    by="Performance_Score",
    ascending=False
)


st.subheader("Top Performers")


top_performers = performance.merge(
    employees[["Employee_ID","Employee_Name","Department"]],
    on="Employee_ID"
).head(10)


st.dataframe(
    top_performers[
        [
"Employee_ID",
"Employee_Name",
"Department",
"Attendance_Percentage",
"Average_Working_Hours",
"Late_Days",
"Performance_Score"
        ]
    ]
)


fig, ax = plt.subplots(figsize=(10,4))


ax.bar(
    top_performers["Employee_ID"].astype(str),
    top_performers["Performance_Score"]
)


ax.set_xlabel("Employee ID")
ax.set_ylabel("Performance Score")
ax.set_title("Top 10 Employee Performance")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Late Arrival Analysis
# -----------------------------

st.subheader("Late Arrival Analysis")


fig, ax = plt.subplots(figsize=(10,4))


ax.bar(
    attendance.sort_values(
    by="Late_Days",
    ascending=False
).head(20)["Employee_ID"].astype(str),
    attendance.sort_values(
    by="Late_Days",
    ascending=False
).head(20)["Late_Days"]
)


ax.set_xlabel("Employee ID")
ax.set_ylabel("Late Days")
ax.set_title("Frequent Late Arrivals")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Leave Utilization Analysis
# -----------------------------

st.subheader("Leave Utilization")


leave_summary = leave["Leave_Type"].value_counts()


fig, ax = plt.subplots(figsize=(7,4))


ax.bar(
    leave_summary.index,
    leave_summary.values
)


ax.set_xlabel("Leave Type")
ax.set_ylabel("Number of Leaves")
ax.set_title("Leave Utilization Analysis")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Department-wise Attendance Analysis
# -----------------------------

st.subheader("Department-wise Attendance")


department_attendance = attendance.merge(
    employees[
        ["Employee_ID", "Department"]
    ],
    on="Employee_ID",
    how="left"
)


department_summary = department_attendance.groupby(
    "Department"
)["Attendance_Percentage"].mean()


fig, ax = plt.subplots(figsize=(8,4))


ax.bar(
    department_summary.index,
    department_summary.values
)


ax.set_xlabel("Department")
ax.set_ylabel("Average Attendance %")
ax.set_title("Department Comparison")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Department Employee Count
# -----------------------------

st.subheader("Employees by Department")


department_count = employees[
    "Department"
].value_counts()


fig, ax = plt.subplots(figsize=(8,4))


ax.bar(
    department_count.index,
    department_count.values
)


ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
ax.set_title("Department Distribution")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Salary Deduction Analysis
# -----------------------------

st.subheader("Salary Deduction Analysis")


fig, ax = plt.subplots(figsize=(10,4))


ax.bar(
    salary["Employee_ID"].head(20).astype(str),
    salary["Deduction"].head(20)
)


ax.set_xlabel("Employee ID")
ax.set_ylabel("Deduction Amount")
ax.set_title("Salary Deduction")


plt.xticks(rotation=45)


st.pyplot(fig)



# -----------------------------
# Salary Summary
# -----------------------------

st.subheader("Salary Report")


st.dataframe(
    salary
)