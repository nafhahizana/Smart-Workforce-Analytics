import pickle
import pandas as pd


model = pickle.load(open("models/performance_model.pkl", "rb"))



employee = {
    "Age": 29,
    "Salary": 65000,
    "Experience": 5,
    "Department_Finance": False,
    "Department_HR": False,
    "Department_IT": True,
    "Department_Marketing": False
}



employee_data = pd.DataFrame([employee])


print("Employee Details:")
print(employee_data)



prediction = model.predict(employee_data)


print("\nPredicted Performance Score:")
print(round(prediction[0], 2))