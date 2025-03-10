import numpy as np
import matplotlib.pyplot as plt

 

# параметры
A = 101            #амплитуда когда нет аномалепроводящего тела
B = 5            #амплитуда для проводящего тела               
tau =0.1 # Постоянная времени (в секундах)  чем больше, тем медленнее затухает, что в свою очередь показывает проводящее тело

# Диапазон времени
t = np.logspace(0, 1, 10)  # От 1 до 10 секунд

# Вычисляем значения функций
P_t = A * t**(-3/2)  # Степенной закон
E_t = B * np.exp(-t / tau)  # Экспоненциальное затухание

# Строим графики
plt.figure(figsize=(6,8))
plt.plot(t, P_t, label=r'$P(t) = A \cdot t^{-3/2}$ (Степенное затухание)', linestyle='--', color='b')
plt.plot(t, E_t, label=r'$E(t) = B \cdot e^{-t/\tau}$ (Экспоненциальное затухание)', linestyle='-', color='r')

# Настройки графика
plt.xscale('log')  # Логарифмическая шкала времени
plt.yscale('log')  # Логарифмическая шкала амплитуды
plt.xlabel('Время (сек)')
plt.ylabel('Амплитуда (пТ)')
plt.title('Сравнение степенного и экспоненциального затухания')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Отображаем график
plt.show()
