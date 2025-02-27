import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid as cumtrapz

# Для воспроизводимости результатов
np.random.seed(0)

# Задаем параметры модели
A = 500.0      # Амплитуда экспоненциального затухания (в пТ)
tau = 0.1     # Константа затухания (в секундах)

# Уровень шума для системы dB/dt (например, 0.3 нТ/с)
noise_level = 0.3  # нТ/с

# Создаем временной массив от 1 мс до 300 мс (500 точек)
t = np.linspace(0.001, 0.3, 500)  # время в секундах

# Вычисляем истинный сигнал dB/dt (в пТ/с), затем преобразуем в нТ/с (умножая на 0.001)
dBdt_true = - (A/tau) * np.exp(-t/tau)           # в пТ/с
dBdt_true_nT = 0.001 * dBdt_true                   # в нТ/с

# Истинное магнитное поле B(t) (в пТ)
B_true = A * np.exp(-t/tau)

# Моделируем измеренный сигнал dB/dt, добавляя гауссовский шум
noise = np.random.normal(0, noise_level, size=t.shape)
dBdt_measured_nT = dBdt_true_nT + noise

# Сигнал dB/dt в измерениях может быть "заслонён" шумом
# Теперь преобразуем измеренный dB/dt в B(t) путём численного интегрирования:
# B(t) = ∫ (dB/dt) dt. Здесь интегрируем измеренный сигнал, полученный в нТ/с.
B_measured_nT = cumtrapz(dBdt_measured_nT, t, initial=0)
# Переводим B из нТ в пТ (1 нТ = 1000 пТ)
B_measured = B_measured_nT * 1000

# Визуализация результатов:
plt.figure(figsize=(14, 6))

# График 1: dB/dt (полезный сигнал скрыт шумом)
plt.subplot(1, 2, 1)
plt.plot(t*1000, dBdt_measured_nT, 'b.', label="Измеренный dB/dt (с шумом)")
plt.plot(t*1000, dBdt_true_nT, 'r-', linewidth=2, label="Истинный dB/dt")
plt.xlabel("Время, мс")
plt.ylabel("dB/dt (нТ/с)")
plt.title("Измерения dB/dt с интерференцией")
plt.legend()
plt.grid(True)

# График 2: Преобразованный сигнал B(t)
plt.subplot(1, 2, 2)
plt.plot(t*1000, B_measured, 'g.', label="Преобразованный B (из dB/dt)")
plt.plot(t*1000, B_true, 'orange', linewidth=2, label="Истинный B")
plt.xlabel("Время, мс")
plt.ylabel("B (пТ)")
plt.title("Интегрированный сигнал B(t)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()