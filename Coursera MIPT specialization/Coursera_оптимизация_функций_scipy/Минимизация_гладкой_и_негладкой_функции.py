import scipy as sc
import scipy.optimize
import math
import numpy as np


# Гладкая функция
def f(x):
    return math.sin(float(x) / 5) * math.exp(float(x) / 10) + 5 * math.exp(-float(x) / 2)


# Негладкая функция
def h(x):
    return int(f(x))


# Локальная оптимизация (тип метода настроить)
x0 = np.array([30]) #numpy-вектор для задания координат точки, к которой ищем ближайший ЛОКАЛЬНЫЙ минимум
res = sc.optimize.minimize(f, x0, method='BFGS')
print(res.x[0])
print('%.2f' %f(res.x[0]))

# Глобальная минимизация - дифференциальная эволюция
x0 = [(1,30)] #список кортежей для задания ограничений на значения параметров оптимизируемой функции
res = sc.optimize.differential_evolution(f, x0)
print(res.x[0])
print('%.2f' %f(res.x[0]))

# Оптимизация негладкой функции
x0 = np.array([30])
res = sc.optimize.minimize(h, x0, method='BFGS')
print(res.x[0])
print(h(res.x[0]))

x0 = [(1,30)]
res = sc.optimize.differential_evolution(h, x0)
print(res.x[0])
print(h(res.x[0]))