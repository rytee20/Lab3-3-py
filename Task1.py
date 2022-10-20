def reducer(f_fraction):  # функция сокращения дроби

    f_numerator = f_fraction[0]  # числитель
    f_denumerator = f_fraction[1]  # знаменатель
    divider = f_numerator  # делитель
    while divider != 0:  # пока делитель не равен нулю
        if f_numerator % divider == 0 and f_denumerator % divider == 0 and divider != 1:  # проверяем делятся ли числитель и знаменатель на него
            f_numerator = f_numerator//divider  # если да то делим их нацело
            f_denumerator = f_denumerator//divider
            divider = f_numerator  # меняем значене делителя
        else:
            divider = divider-1  # иначе просто уменьшаем его
    f_reduced_fraction = (f_numerator, f_denumerator)  # создам кортеж и возвращаем его
    return f_reduced_fraction


numerator = 0  # числитель
denumerator = 0  # знаменатель

while True:  # ввод числителя с проверкой
        try:
            while numerator <= 0:
                numerator = int(input("Введите числитель дроби: "))
            break
        except ValueError:
            print("Вы ввели не верно. Попробуйте снова: ")

while True:  # ввод с знаменателя с проверкой
        try:
            while denumerator <= numerator or denumerator == 0:
                denumerator = int(input("Введите знаменатель дроби, он должен быть больше числителя: "))
            break
        except ValueError:
            print("Вы ввели не верно. Попробуйте снова: ")

fraction = (numerator, denumerator)  # создаем кортеж исходной дроби
reduced_fraction = reducer(fraction)  # сокращам ее
print("Результат: ")  # вывод
print("m' = ", reduced_fraction[0], "; n' = ", reduced_fraction[1])
