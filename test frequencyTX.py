import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
A = 0.004     # Амплитуда степенного затухания
B = 5         # Амплитуда экспоненциального затухания (для tau=0.1)
tau = 0.1     # Постоянная времени (в секундах)
frequencies = [0.125, 0.25, 0.5, 1, 2, 4, 8, 16]  # Частоты передатчика (Гц)

# Функция идеального отклика
def step_response(t):
    return A * t**(-1.5) + B * np.exp(-t / tau)

# Временная сетка (off-time)
t_off = np.logspace(-3, 0, 100)  # От 1 мс до 1 с в логарифмическом масштабе

# Расчет сигнала для каждой частоты
plt.figure(figsize=(12, 8))

for freq in frequencies:
    T = 1 / freq               # Период
    duty_cycle = 0.5           # Скважность 50%
    t_active = T * duty_cycle  # Время активности передатчика
    
    # Суммарный сигнал с учетом предыдущих импульсов
    V = np.zeros_like(t_off)
    for n in range(0, 5):       # Учитываем 5 предыдущих периодов
        t_total = t_off + n * T
        valid = t_total > t_active  # Учитываем только off-time
        V[valid] += step_response(t_total[valid] - t_active)
    
    # Построение графика
    plt.loglog(t_off, V, label=f'f={freq} Hz')

plt.title(f'Зависимость сигнала от частоты (tau={tau} сек)')
plt.xlabel('Время (сек)')
plt.ylabel('Амплитуда (пТл)')
plt.legend()
plt.grid(True)
plt.show()