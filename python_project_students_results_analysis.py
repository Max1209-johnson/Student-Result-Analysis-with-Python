# -*- coding: utf-8 -*-
"""Python Project- Students Results Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16KLtZNiQnOoYFEaKiCHI2LrJFWJfIyCy
"""

!pip install numpy
!pip install pandas
!pip install matplotlib
!pip install seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_scores.csv")
print(df.head())

df. describe()

df.info()

df.isnull().sum()

#drop unnamed column

df = df.drop("Unnamed: 0", axis=1)
print(df.head())

plt.figure(figsize=(4,5))
ax = sns.countplot(data= df, x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender distributions")
plt.show

# from the above chart we have analysed that: the number of females are more in data

gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":"mean"})
print(gb)

plt.figure(figsize=(2,2))
sns.heatmap(gb, annot =True)
plt.title("Relationship between Parent's Education and student's SScore ")
plt.show()

gb1 = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":"mean"})
print(gb1)

plt.figure(figsize=(2,2))
sns.heatmap(gb1, annot =True)
plt.title("Relationship between Parent's Education and student's SScore ")
plt.show()

# from the above chart we conculde that there is no impact on childrens on basis of marriage status

sns.boxplot(data =df, x ="MathScore")
plt.title("MathScore")
plt.show()

sns.boxplot(data =df, x ="ReadingScore")
plt.title("ReadingScore")
plt.show()

sns.boxplot(data =df, x ="WritingScore")
plt.title("WritingScore")
plt.show()

print(df["EthnicGroup"].unique())

groupA = df.loc[(df['EthnicGroup'] == "Group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "Group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "Group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "Group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "Group E")].count()

plt.pie

plt.show()