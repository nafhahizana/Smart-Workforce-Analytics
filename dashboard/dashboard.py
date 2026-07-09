import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Smart Workforce Analytics",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Smart Workforce Analytics")

st.write(
    "An AI-powered dashboard for analyzing employee performance, "
    "salary distribution, and workforce insights."
)


# Load dataset
data = pd.read_csv("dataset/employees.csv")


# Sidebar
st.sidebar.header("Employee Filters")

department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(data["Department"].unique())
)


# Apply filter
if department != "All":
    filtered_data = data[data["Department"] == department]
else:
    filtered_data = data



# Employee Data
st.subheader("👥 Employee Data")

st.dataframe(filtered_data)



# Statistics
st.subheader("📈 Workforce Statistics")

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Total Employees",
        len(filtered_data)
    )


with col2:
    st.metric(
        "Average Salary",
        f"₹ {filtered_data['Salary'].mean():,.0f}"
    )


with col3:
    st.metric(
        "Average Performance",
        f"{filtered_data['Performance_Score'].mean():.1f}"
    )



# Salary Analysis
st.subheader("💰 Salary Analysis")

fig, ax = plt.subplots()

ax.bar(
    filtered_data["Name"],
    filtered_data["Salary"]
)

ax.set_xlabel("Employee Name")
ax.set_ylabel("Salary")
ax.set_title("Employee Salary Distribution")

plt.xticks(rotation=45)

st.pyplot(fig)



# Performance Analysis
st.subheader("⭐ Performance Analysis")

fig, ax = plt.subplots()

ax.bar(
    filtered_data["Name"],
    filtered_data["Performance_Score"]
)

ax.set_xlabel("Employee Name")
ax.set_ylabel("Performance Score")
ax.set_title("Employee Performance")

plt.xticks(rotation=45)

st.pyplot(fig)



# Department Analysis
st.subheader("🏢 Department Analysis")

department_count = filtered_data["Department"].value_counts()

fig, ax = plt.subplots()

ax.bar(
    department_count.index,
    department_count.values
)

ax.set_xlabel("Department")
ax.set_ylabel("Employees")
ax.set_title("Employees by Department")

st.pyplot(fig)



# ML Prediction Section

import pickle


st.subheader("🤖 Performance Prediction")


# Load trained model
model = pickle.load(
    open("models/performance_model.pkl", "rb")
)


age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=25
)


salary = st.number_input(
    "Salary",
    min_value=10000,
    max_value=200000,
    value=50000
)


experience = st.number_input(
    "Experience",
    min_value=0,
    max_value=40,
    value=3
)


department = st.selectbox(
    "Department",
    [
        "Finance",
        "HR",
        "IT",
        "Marketing"
    ]
)


# Create input data

input_data = pd.DataFrame(
    {
        "Age":[age],
        "Salary":[salary],
        "Experience":[experience],
        "Department_Finance":[department=="Finance"],
        "Department_HR":[department=="HR"],
        "Department_IT":[department=="IT"],
        "Department_Marketing":[department=="Marketing"]
    }
)


if st.button("Predict Performance"):

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Performance Score: {prediction[0]:.1f}"
    )



    # Employee Insights

st.subheader("🏆 Employee Insights")


top_employee = data.loc[
    data["Performance_Score"].idxmax()
]


highest_salary = data.loc[
    data["Salary"].idxmax()
]


col1, col2 = st.columns(2)


with col1:
    st.info(
        f"⭐ Top Performer: {top_employee['Name']} "
        f"(Score: {top_employee['Performance_Score']})"
    )


with col2:
    st.info(
        f"💰 Highest Salary: {highest_salary['Name']} "
        f"(₹{highest_salary['Salary']})"
    )



# Ranking Table

st.subheader("📊 Performance Ranking")


ranking = data.sort_values(
    by="Performance_Score",
    ascending=False
)


st.dataframe(ranking)



# Download Report

csv = ranking.to_csv(index=False)


st.download_button(
    label="📥 Download Employee Report",
    data=csv,
    file_name="employee_report.csv",
    mime="text/csv"
)