def hofstadter_f_m(n: int) -> tuple[int, int]:  # функция сокращения дроби
    if n ==0:
        yield
    else:
        f = [1]
        m = [0]
        for i in range(1,n):
            m.append(i-f[m[i-1]])
            f.append(i - m[f[i - 1]])
        for i in range(0, n):
            yield f[i], m[i]


n = 0  #

while True:  # ввод  с проверкой
        try:
            while n <= 0:
                n = int(input("Введите: "))
            break
        except ValueError:
            print("Вы ввели не верно. Попробуйте снова: ")

for f_m in hofstadter_f_m(n):
    print(f_m, end=', ')
