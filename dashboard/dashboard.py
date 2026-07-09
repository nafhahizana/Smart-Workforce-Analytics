import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart Workforce Analytics")

data = pd.read_csv("dataset/employees.csv")

# Employee Data
st.subheader("Employee Data")
st.dataframe(data)



st.subheader("Workforce Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Employees", len(data))

with col2:
    st.metric("Average Salary", f"{data['Salary'].mean():.0f}")

with col3:
    st.metric("Average Performance", f"{data['Performance_Score'].mean():.1f}")



st.subheader("Employee Salary Analysis")

fig, ax = plt.subplots()

ax.bar(data["Name"], data["Salary"])

ax.set_xlabel("Employee Name")
ax.set_ylabel("Salary")
ax.set_title("Salary Analysis")

st.pyplot(fig)



st.subheader("Employee Performance Analysis")

fig, ax = plt.subplots()

ax.bar(data["Name"], data["Performance_Score"])

ax.set_xlabel("Employee Name")
ax.set_ylabel("Performance Score")
ax.set_title("Performance Analysis")

st.pyplot(fig)



st.subheader("Department Analysis")

department_count = data["Department"].value_counts()

fig, ax = plt.subplots()

ax.bar(department_count.index, department_count.values)

ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
ax.set_title("Employees by Department")

st.pyplot(fig)