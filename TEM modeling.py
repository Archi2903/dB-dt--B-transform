import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры
P = 0.02      # Амплитуда степенного затухания (в пТ)
E = 25.0      # Амплитуда экспоненциального затухания (в пТ)
tau = 0.1     # Постоянная времени (в секундах)

# Создаем временной массив (логарифмически распределенный)
t = np.logspace(-3, -0.5, 500)  # от 1 мс до ~0.316 сек

# Вычисляем dB/dt и B(t)
dBdt = -0.001 * ((3/2) * P * t**(-5/2) + (E/tau) * np.exp(-t/tau))
B =(P * t**(-3/2) + E * np.exp(-t/tau))

# Построение графиков
plt.figure(figsize=(8, 6))
plt.loglog(t, np.abs(dBdt), 'b-', label='|dB/dt| (нТ/с)')
plt.loglog(t, B, 'r-', label='B(t) (пТ)')
plt.xlabel('Время t (сек)')
plt.ylabel('Значение')
plt.title('Сравнение dB/dt и B(t)')
plt.grid(True, which='both', ls='--')
plt.legend()
plt.show()
