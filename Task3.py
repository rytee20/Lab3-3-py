from datetime import date, timedelta
import random


def nearest_date(*dates):
    current_date = date.today()
    near_date = date(dates[0].year, dates[0].month, dates[0].day)
    for i_date in dates:
        if abs(i_date - current_date) < abs(near_date - current_date):
            near_date = i_date
        else:
            if abs(i_date - current_date) == abs(near_date - current_date):
                near_date = max(i_date, near_date)
    print("Ближайшая дата из всех: ", near_date)


date1 = date(2020, 10, 1)
date2 = date(2022, 10, 13)
date3 = date(2022, 10, 9)
nearest_date(date1, date2, date3)
