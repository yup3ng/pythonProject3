import pandas as pd
from matplotlib import pyplot as plt


class Chart:
    countries = pd.read_excel(r"/Users/yup3ng/Downloads/Project_File_Python.xlsx")

Chart()
country_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(Chart.countries)
Asia = Chart.countries
Asia = Asia.iloc[:, lambda Asia: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
asia = Asia.set_index("Unnamed: 0")
asia = asia.loc["1998 Jan":"2007 Dec"]
print(asia)

Sum = asia.sum(axis=0)
Sum = Sum.sort_values(ascending=True)
print(Sum)

Top1 = Sum.index[0]
Top2 = Sum.index[1]
Top3 = Sum.index[2]

top1 = Sum[Top1]
top2 = Sum[Top2]
top3 = Sum[Top3]

Mean = asia.mean(axis=0)
Mean = Mean.sort_values(ascending=True)
print(Mean)

Mean1 = round(Mean[0],2)
Mean2 = round(Mean[1],2)
Mean3 = round(Mean[2],2)

Median = asia.median(axis=0)
Median = Median.sort_values(ascending=True)
print(Median)

median1 = Median[0]
median2 = Median[1]
median3 = Median[2]

print("Lowest 3 Countries with the most Visitors:", Top1, Top2, Top3)
print("Visitor numbers from Lowest 3 Countries:", top1, top2, top3)
print("Mean visitor numbers from Lowest 3 Countries", Mean1, Mean2, Mean3)
print("Median visitor numbers from Lowest 3 Countries:", median1, median2, median3)

import numpy as np
date_sum = asia.sum(axis=1)
month = np.zeros((12,), dtype=int).tolist()
month_name = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
for j in range(0,12):
        for i in np.arange(j,119,12):
            month[j] += date_sum.iat[i]
print(month)
plt.plot(month_name,month)
plt.show()