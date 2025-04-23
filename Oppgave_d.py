import numpy as np
import statsmodels as sm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

fil = "student_performance_dataset.csv"
data = pd.read_csv(fil)
dataframe1 = pd.DataFrame(data)

#Omgjøre yes/no til 1/0, så vi kan regne ut
binære_kollonner = ["Internet_Access_at_Home", "Extracurricular_Activities"]
dataframe1[binære_kollonner] = dataframe1[binære_kollonner].applymap(lambda x: 1 if x == "Yes" else 0)

#latex output for kontinuerlige variablene, analyse
latex_output = dataframe1[[
    'Study_Hours_per_Week',
    'Attendance_Rate',
    'Past_Exam_Scores'
]].describe().style.format(precision=3).to_latex()
print(latex_output)

#for å danne diagram for variablene
binære_vaiabler = ["Gender","Internet_Access_at_Home", "Extracurricular_Activities" ]
for var in binære_vaiabler:
    sns.countplot(data=dataframe1, x=var)
    plt.title(f"Fordeling av {var.replace('_', ' ')}")
    plt.xlabel(var.replace('_', ' '))
    plt.ylabel("Antall")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
