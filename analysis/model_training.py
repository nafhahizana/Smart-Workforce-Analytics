import pandas as pd

data = pd.read_csv("dataset/cleaned_employees.csv")

print("Cleaned Dataset")
print(data)

X = data.drop("Performance_Score", axis=1)

y = data["Performance_Score"]

print("\nInput Features:")
print(X)

print("\nTarget:")
print(y)



from sklearn.model_selection import train_test_split

# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)



from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


model = RandomForestRegressor(random_state=42)


model.fit(X_train, y_train)

print("\nModel Training Completed!")


y_pred = model.predict(X_test)

print("\nPredicted Values:")
print(y_pred)


mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error:")
print(mae)

print("\nR2 Score:")
print(r2)



import pickle
import os


os.makedirs("models", exist_ok=True)


with open("models/performance_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("\nModel saved successfully!")