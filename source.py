import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('full_data.csv')
data = data.drop(['biweekly_cases', 'biweekly_deaths'], axis=1)
data = data.loc[data["new_deaths"] != 1.0]
#convert_dict = {'new_deaths': int, 'new_cases': int, 'total_deaths': int, 'weekly_cases': int, 'weekly_deaths': int}
#data = data.astype(convert_dict)
print('---> Raw data shape: ', data.shape)

egypt_cases = data[data["location"] == 'Egypt']
egypt_cases = egypt_cases.drop(['new_deaths', 'total_deaths', 'weekly_deaths'], axis=1)
egypt_cases = egypt_cases.loc[data["new_cases"] > 0.0]
egypt_cases = egypt_cases.loc[data["weekly_cases"] > 0.0]
egypt_cases['date'] = pd.to_datetime(egypt_cases['date'], format="%Y-%m-%d %H:%M:%S")
egypt_cases['year']= egypt_cases['date'].dt.year
egypt_cases['month']= egypt_cases['date'].dt.month
print('___________________________________________________________________________________________________________________')
print('------------------------------------------------------NEW RUN------------------------------------------------------')
print('-------------------------------------------------------------------------------------------------------------------')
print(egypt_cases.head(20))
#print(egypt_cases.dtypes)
# RETREIVE CASES IN 2020, 2021, 2022 ONLY

egypt_cases_2020 = egypt_cases.loc[:, ['year', 'month', 'new_cases']]
egypt_cases_2020 = egypt_cases_2020.loc[egypt_cases_2020['year'] == 2020]
egypt_cases_2020 = egypt_cases_2020.groupby('month', axis=0).sum('new_cases')
print(egypt_cases_2020.head(20))

egypt_cases_2021 = egypt_cases.loc[:, ['year', 'month', 'new_cases']]
egypt_cases_2021 = egypt_cases_2021.loc[egypt_cases_2021['year'] == 2021]
egypt_cases_2021 = egypt_cases_2021.groupby('month', axis=0).sum('new_cases')
print(egypt_cases_2021.head(20))

egypt_cases_2022 = egypt_cases.loc[:, ['year', 'month', 'new_cases']]
egypt_cases_2022 = egypt_cases_2022.loc[egypt_cases_2022['year'] == 2022]
egypt_cases_2022 = egypt_cases_2022.groupby('month', axis=0).sum('new_cases')
print(egypt_cases_2022.head(20))

plt.figure(0)
egypt_cases_2020_plot_x_axis = np.array(range(3,13))
egypt_cases_2020_plot_y_axis = np.array(egypt_cases_2020['new_cases'])
egypt_cases_2020_plot = plt.title("COVID-19 CASES IN EGYPT, 2020")
egypt_cases_2020_plot = plt.xlabel("Month")
egypt_cases_2020_plot = plt.ylabel("Cases per month")
egypt_cases_2020_plot = plt.bar(egypt_cases_2020_plot_x_axis, egypt_cases_2020_plot_y_axis)

plt.figure(1)
egypt_cases_2021_plot_x_axis = np.array(range(1,13))
egypt_cases_2021_plot_y_axis = np.array(egypt_cases_2021['new_cases'])
egypt_cases_2021_plot = plt.title("COVID-19 CASES IN EGYPT, 2021")
egypt_cases_2021_plot = plt.xlabel("Month")
egypt_cases_2021_plot = plt.ylabel("Cases per month")
egypt_cases_2021_plot = plt.bar(egypt_cases_2021_plot_x_axis, egypt_cases_2021_plot_y_axis)

plt.figure(2)
egypt_cases_2022_plot_x_axis = np.array(range(1,5))
egypt_cases_2022_plot_y_axis = np.array(egypt_cases_2022['new_cases'])
egypt_cases_2022_plot = plt.title("COVID-19 CASES IN EGYPT, 2022")
egypt_cases_2022_plot = plt.xlabel("Month")
egypt_cases_2022_plot = plt.ylabel("Cases per month")
egypt_cases_2022_plot = plt.bar(egypt_cases_2022_plot_x_axis, egypt_cases_2022_plot_y_axis)

plt.figure(3)
egypt_cases_plot_x_axis = np.array(range(1, 733))
egypt_cases_plot_y_axis = np.array(egypt_cases['new_cases'])
egypt_cases_plot = plt.title("COVID-19 CASES IN EGYPT BY DAY 2020-2022")
egypt_cases_plot = plt.xlabel("Days since Covid-19 spread in Egypt")
egypt_cases_plot = plt.ylabel("Cases per day")
egypt_cases_plot = plt.plot(egypt_cases_plot_x_axis, egypt_cases_plot_y_axis)
plt.show()
