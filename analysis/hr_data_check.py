import pandas as pd


files = [
    "employee_master.csv",
    "attendance.csv",
    "leave_records.csv",
    "salary.csv"
]


for file in files:

    print("\n")
    print("=" * 40)
    print(file.upper())
    print("=" * 40)

    data = pd.read_csv(
        "dataset/" + file
    )

    print("\nFirst 5 Rows:")
    print(data.head())

    print("\nShape:")
    print(data.shape)

    print("\nMissing Values:")
    print(data.isnull().sum())

    print("\nDuplicate Rows:")
    print(data.duplicated().sum())

    print("\nData Types:")
    print(data.dtypes)