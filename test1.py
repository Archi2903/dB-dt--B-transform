import numpy as np
import matplotlib.pyplot as plt

def step_response(t, A, B, tau):
    """
    Идеализированный отклик S(t):
      S(t) = A * t^(-1.5) + B * exp(-t/tau) для t >= 0, и 0 для t < 0.
    """
    S = np.zeros_like(t)
    mask = t > 0
    S[mask] = A * t[mask]**(-1.5) + B * np.exp(-t[mask] / tau)
    return S

def transmitter_pulse(t, T, duty_cycle):
    """
    Функция окна: возвращает 1, если (t mod T) < duty_cycle*T, иначе 0.
    """
    return np.where((t % T) < duty_cycle * T, 1.0, 0.0)

def simulate_tem(f_tx, f_rx, A, B, tau, duty_cycle=0.5, t_max=1.0):
    """
    Моделирует измеряемый сигнал TEM:
      X_f(t) = sum_{n=0}^{N} [S(t - nT) * w(t - nT; T, duty_cycle)],
    где T = 1/f_tx — период импульсов передатчика.
    
    Параметры:
      f_tx      - частота передатчика (Гц)
      f_rx      - частота дискретизации (приёмника, Гц)
      A, B, tau - параметры отклика S(t)
      duty_cycle- активная часть периода (например, 0.5)
      t_max     - длительность моделирования (с)
    """
    T = 1.0 / f_tx
    dt = 1.0 / f_rx
    t_full = np.arange(0, t_max, dt)
    s_meas = np.zeros_like(t_full)
    
    n_max = int(np.ceil(t_max / T))
    for n in range(n_max):
        t_shifted = t_full - n * T
        # Вычисляем отклик S(t - nT)
        response = step_response(t_shifted, A, B, tau)
        # Множитель окна: учитываем, что измерение происходит только в активном окне
        window = transmitter_pulse(t_shifted, T, duty_cycle)
        s_meas += response * window
    
    return t_full, s_meas

# Параметры модели
A = 0.004       # амплитуда степенного затухания
B = 5.0         # амплитуда экспоненциального затухания (в условных единицах)
tau = 0.1       # постоянная времени экспоненциального затухания (с)
duty_cycle = 0.5  # 50% duty-cycle
t_max = 1.0      # моделируем 1 секунду
f_rx = 1000      # частота дискретизации (приёмника) 1000 Гц

# Различные частоты передатчика для демонстрации
freqs = [0.125, 0.25, 0.5, 1, 2, 4, 8, 16]

plt.figure(figsize=(10, 8))
for f_tx in freqs:
    t, s = simulate_tem(f_tx, f_rx, A, B, tau, duty_cycle, t_max)
    plt.plot(t, s, label=f'f_tx = {f_tx} Hz')

plt.xlabel('Time (s)')
plt.ylabel('Measured Signal (a.u.)')
plt.title('Влияние частоты передатчика на TEM-сигнал')
plt.legend()
plt.grid(True)
plt.show()
