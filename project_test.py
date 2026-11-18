import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("test.csv")

def make_main_life(mlife):
    if "False" in mlife:
        return np.nan
    return int(mlife) 


def make_main_people(mpeople):
    if "False" in mpeople:
        return np.nan
    return int(mpeople)

df["life_main"] = df["life_main"].apply(make_main_life)
df["people_main"] = df["people_main"].apply(make_main_people)

filtered = df[
    (df["sex"] == 1) & 
    (df["people_main"] == 1) &
    (df["life_main"] >= 1)
]


quantity = [20,7,3,2,1,1]
category = ["Саморозвиток", "Сім'я і діти","Вдосконалення світу","Краса і мистецтво","Наука і дослідження","Розлучення і відпочинок"]
pd.Series(quantity, index=category).plot(kind='barh',figsize=(12,6) ,grid= True, color = "#1cf3e5")
plt.title("Життєві пріоритети", fontsize=16, color="black")
plt.xlabel("Кількість людей", fontsize=13, color="black")
plt.ylabel("Категорії", fontsize=13, color="black")
plt.xticks(fontsize=9, color="black")
plt.yticks(fontsize=9, color="black")
plt.tight_layout()
plt.show()

