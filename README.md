# Smart Workforce Analytics

## Project Overview

Smart Workforce Analytics is an AI-powered employee analytics system that analyzes workforce data, predicts employee performance, and provides interactive insights through a Streamlit dashboard.

The project uses Machine Learning and Data Analytics techniques to understand employee performance based on age, salary, experience, and department.

---

## Features

- Employee data analysis
- Data quality checking
- Data cleaning and preprocessing
- Salary analysis
- Performance analysis
- Department-wise workforce insights
- Machine Learning performance prediction
- Interactive Streamlit dashboard
- Employee report download

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Git & GitHub

---

## Project Structure

Smart-Workforce-Analytics/

│
├── analysis/
│ ├── data_check.py
│ ├── data_quality.py
│ ├── data_cleaning.py
│ ├── model_training.py
│ └── predict_performance.py
│
├── charts/
│
├── dashboard/
│ └── dashboard.py
│
├── dataset/
│
├── models/
│ └── performance_model.pkl
│
├── exports/
│
├── app.py
├── requirements.txt
└── README.md

---

## How to Run

Install required packages:

pip install -r requirements.txt


Run dashboard:

python -m streamlit run dashboard/dashboard.py


---

## Machine Learning Model

The project uses a machine learning regression model to predict employee performance scores.

Input features:

- Age
- Salary
- Experience
- Department

Output:

- Performance Score

---

## Dashboard Preview

The dashboard provides:

- Workforce statistics
- Salary charts
- Performance charts
- Department analysis
- ML prediction system

---

## Author

Nafha Hizana