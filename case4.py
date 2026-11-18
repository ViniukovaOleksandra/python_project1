import pandas as pd    
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("DataAnalyst2.csv")

def make_location(location):
    return(location[-2:])

df["Location"] = df["Location"].apply(make_location)

def make_salary(salary):
    try:
        if "Glassdoor est." in salary:
            salary2 = salary.replace(" (Glassdoor est.)", "").replace("$","").replace("K","")
            min_salary_str, max_salary_str = salary2.split("-")
            max_salary = int(max_salary_str)
            min_salary = int(min_salary_str)
            avg_salary = (max_salary + min_salary) // 2
            salary3 = avg_salary * 1000
            return salary3
        else:
            return np.nan 
    except:
        return np.nan 
df["Salary Estimate"] = df["Salary Estimate"].apply(make_salary)
filtered = df[
    (df["Location"] == "CA") &
    (df["Type of ownership"] == 'Company - Private') &
    (df["Founded"].fillna(0).astype(int) >= 1995)

]

print(df["Salary Estimate"].quantile(0.75))
high_salary = filtered[filtered["Salary Estimate"] >= 80000].shape[0]
other_salary = filtered[filtered["Salary Estimate"] < 80000].shape[0]
values = [high_salary, other_salary]
labels = ["Високі зарплати", "Інші"]
pd.Series(values, index=labels).plot(kind='barh',figsize=(12,6) ,grid= True)
plt.show()

