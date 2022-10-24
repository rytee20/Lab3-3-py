from datetime import date, timedelta


def nearest_date(*dates):  # функция поиска ближайшей даты
    current_date = date.today()  # смотрим сегодняшнюю
    near_date = date(dates[0].year, dates[0].month, dates[0].day)  # в ближайшую дату записывам первую
    for i_date in dates:  # и идем по порядку
        if abs(i_date - current_date) < abs(near_date - current_date):  # если разница текущей и данной меньше чем текущей и "ближайшей"
            near_date = i_date  # ближайшая=данная
        else:
            if abs(i_date - current_date) == abs(near_date - current_date):  # если разницы равны
                near_date = max(i_date, near_date)  #ближайшая=большей из них
    print("Ближайшая дата из всех: ", near_date)  # вывод


date1 = date(2020, 10, 1)
date2 = date(2022, 10, 13)
date3 = date(2022, 10, 9)
nearest_date(date1, date2, date3)
