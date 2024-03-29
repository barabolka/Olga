import numpy as np
import matplotlib.pyplot as plt
import decimal
import math
'''
рівняння вводимо рівне 0 без правої частини.
наприклад для введення x ** 2 + 4 * x-8 = 0 вводимо x ** 2 + 4 * x-8
'''

e = float(input("значення вхідної помилки розрахунку e = "))  # ввести точність обчислень
if e > 0.001:  # перевіряємо, щоб точність була вище.
    # для багатьох функція ірраціональний відповідь, потрібна підвищена точність
    print("буде велика помилка розв'язання рівняння")

funk = input("введіть рівняння: ")  # ввести рівняння за прикладом коментаря ''' вище
x = float(input("вхідне кореневе рівняння: "))  # ввести зразкову рішення рівняння


# для початку обчислень

# вводимо функцію обчислення значення
# похідної функції в точці х з точністю e
def deriv(x, e):
    a = eval(funk)
    x = x + e
    b = eval(funk)
    return (b - a) / e


# Функція для метода Ньютона
def newton(funk, x, e):
    df = deriv(x, e)  # значення похідної в точці х, звертаємося до функції deriv()
    while True:  # цикл буде виконуватися до виконання умови z < e
        dx = eval(funk)  # значення функції в точці х
        if df == 0:  # якщо похідна буде дорівнює нулю, то наступне рівняння не
            # буде виконано. обходимо це
            df = e
        y = x - dx / df  # перевірка умови по методу Ньютона
        z = abs(y - x)  # перевірка близькості двох значень (наближення до правильної відповіді)
        if z < e:  # досягнута необхідна точність
            break  # якщо так, то цикл завершеен
        x = y  # беремо нову точку для перевірки
        df = deriv(x, e)  # значення похідної в новій точці х, через функцію deriv()
    return x  # вирішення рівняння


n = newton(funk, x, e)  # звертаємося до функції рішення по методу Ньютона (аргументи
# функція, початкове х і задана точність е

# друкуємо відповідь
print("Solve for x in equation ", funk, " = 0")
print("є x = %0.10f" % n)  #

# кордони для графіка (тут нічого не міняти)
a = n - 1
b = n + 1

# креслимо графік
x = np.arange(a, b, 0.1)
y = eval(funk)
plt.plot(x, y)
plt.show()
