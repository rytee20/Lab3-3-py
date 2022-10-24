def hofstadter_f_m(n: int) -> tuple[int, int]:  # функция-генератор
    if n == 0:
        yield
    else:
        f = [1]  # первые элементы последовательностей
        m = [0]
        for i in range(1, n):  # в зависимости от передаваемого количества
            m.append(i-f[m[i-1]])  # вычисляем элементы по формуле
            f.append(i - m[f[i - 1]])
        for i in range(0, n):  # возвращаем элементы
            yield f[i], m[i]


n = 0  # номер последовательности

while True:  # ввод  с проверкой
        try:
            n = int(input("Введите номер последовательностей: "))
            while n <= 0:
                n = int(input("Вы ввели не верно. Попробуйте снова: \nВведите номер последовательностей: "))
            break
        except ValueError:
            print("Вы ввели не верно. Попробуйте снова: ")

for f_m in hofstadter_f_m(n):  # вывод
    print(f_m, end=' ')
