import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

sampling_rate = 1000
duration = 1.0
fundamental_freq = 5

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

signal = np.zeros_like(t)
for n in range(1, 20, 2):
    harmonic = (1 / n) * np.sin(2 * np.pi * n * fundamental_freq * t)
    signal += harmonic

fft_result = fft(signal)
fft_magnitude = np.abs(fft_result)
fft_phase = np.angle(fft_result)

frequencies = fftfreq(len(t), 1 / sampling_rate)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, signal, label="Сигнал с гармониками")
plt.title("Исходный сигнал")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.grid()
plt.legend()

plt.subplot(3, 1, 2)
plt.stem(frequencies[:len(frequencies)//2], fft_magnitude[:len(frequencies)//2], basefmt=" ")
plt.title("Амплитудный спектр")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(frequencies[:len(frequencies)//2], fft_phase[:len(frequencies)//2], basefmt=" ")
plt.title("Фазовый спектр")
plt.xlabel("Частота (Гц)")
plt.ylabel("Фаза (рад)")
plt.grid()

plt.tight_layout()
plt.show()