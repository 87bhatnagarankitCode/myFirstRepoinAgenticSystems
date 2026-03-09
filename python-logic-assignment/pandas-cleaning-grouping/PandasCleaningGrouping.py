
import pandas as pd
import numpy as np
import os

os.system('cls')

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print(df)
print("**"*70)

print("\n Missing Values:\n", df.isnull(), "\n")
print("**"*70)
print("\n Missing Values  Counts :\n", df.isnull().sum(), "\n")

mean_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(mean_salary)
print("**"*70)
print("post Mean filled",df.isnull().sum(), "\n",df)
df = df.drop(columns=["Temporary_Notes"])
print("dropped column \n",df)
df = df.rename(columns={"Salary": "Annual_Salary"})
print("cleaned dataset post renamed \n",df)

summary = df.groupby("Department").agg({"Annual_Salary": "mean", "Employee": "count"})


print("Summary>>\n",summary)