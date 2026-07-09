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
    st.metric(
        "Total Late Arrivals",
        attendance["Late_Days"].sum()
    )


with col4:
    st.metric(
        "Average Working Hours",
        f"{attendance['Average_Working_Hours'].mean():.2f}"
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
# Late Arrival Analysis
# -----------------------------

st.subheader("Late Arrival Analysis")


fig, ax = plt.subplots(figsize=(10,4))


ax.bar(
    attendance["Employee_ID"].head(20).astype(str),
    attendance["Late_Days"].head(20)
)


ax.set_xlabel("Employee ID")
ax.set_ylabel("Late Days")
ax.set_title("Frequent Late Arrivals")


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
# Department Analysis
# -----------------------------

st.subheader("Department Distribution")


department = employees[
    "Department"
].value_counts()


fig, ax = plt.subplots()


ax.bar(
    department.index,
    department.values
)


ax.set_xlabel("Department")
ax.set_ylabel("Employees")


st.pyplot(fig)



# -----------------------------
# Salary Summary
# -----------------------------

st.subheader("Salary Report")


st.dataframe(
    salary
)