#код моделирует распространение сейсмических волн в скважине:
""" 
1. Генерирует сетку глубин.
2. Вычисляет истинную скорость и медленность.
3. Строит аналитическое и численное решения для времени пробега.
4. Добавляет шум и анализирует его влияние.
"""




import numpy as np # numpy (сокращенно np) — библиотека для работы с массивами и математическими вычислениями.
import matplotlib.pyplot as plt # matplotlib.pyplot (сокращенно plt) — библиотека для построения графиков.

#Определение параметров сетки
# n = 100 — задаем количество уровней измерений (изменяется на 4 в части (e)).
# Number and location of seismometer depths (change n to 4 for part (e))
n = 100  # n = 4 for part (e)

# np.linspace(0, 20, n + 1) — создаем массив из n+1 значений, равномерно распределенных от 0 до 20.
z = np.linspace(0, 20, n + 1)[1:]  # [1:] — убираем первый элемент (нужны только точки от z = 0 до z = 20, но без начального 0).
Deltaz = z[1] - z[0] # Deltaz = z[1] - z[0] — шаг сетки (расстояние между уровнями измерений).

# Velocity gradient
g = 40 # g = 40 — градиент скорости (скорость изменения скорости с глубиной).
# Velocity at z=0
v0 = 1000 # v0 = 1000 — скорость на глубине z = 0.

# True velocity at midpoints
v = v0 + (z - Deltaz / 2) * g # v = v0 + (z - Deltaz / 2) * g — скорость на серединах интервалов.
# True slowness
s = 1 / v # s = 1 / v — истинная медленность.

# Perfect data (analytic solution)
##t = (1 / g) * (np.log(v0 + z * g) - np.log(v0)) # t = (1 / g) * (np.log(v0 + z * g) - np.log(v0)) — аналитическое решение.

# G matrix (discretized solution)
G = np.tril(np.ones((n, n)) * Deltaz) # G = np.tril(np.ones((n, n)) * Deltaz) — матрица G.

# Plot Analytical vs. Discretized Travel Time
plt.figure(1) # plt.figure(1) — создаем новое окно для графика.
##plt.plot(z, t, 'k', label='Analytical SIGNAL') # plt.plot(z, t, 'k', label='Analytical') — строим график аналитического решения.
plt.plot(z, G @ s, 'r-.', label='Discretized SIGNAL') #    plt.plot(z, G @ s, 'r-.', label='Discretized') — строим график дискретизированного решения.
plt.xlabel('Depth(ГЛУБИНА)) (m)') # plt.xlabel('Depth (m)') — подписываем ось x.
plt.ylabel('Travel Time (s)') # plt.ylabel('Travel Time (s)') — подписываем ось y.
plt.legend(loc='lower right') # plt.legend(loc='lower right') — добавляем легенду в правый нижний угол.
plt.grid() # plt.grid() — добавляем сетку.


Plot TTrue vs. Estimated Slowness (Noise-free Solution)
plt.figure(2)
plt.plot(z, s, 'k', label='m_true')
plt.plot(z, np.linalg.solve(G, t), 'r-.', label='m')
plt.xlabel('Depth (m)')
plt.ylabel('Slowness (m/s)')
plt.legend()
plt.title('Noise-free Solution')
plt.grid()

# Add noise to the travel time data vector
tn = t + 0.00005 * np.random.randn(*t.shape)

# Plot True vs. Estimated Slowness (Noisy Solution)
plt.figure(3)
plt.plot(z, s, 'k', label='m_true')
plt.plot(z, np.linalg.solve(G, tn), 'r-.', label='m')
plt.xlabel('Depth (m)')
plt.ylabel('Slowness (m/s)')
plt.legend()
plt.title('Noisy Solution')
plt.grid()
plt.show()
