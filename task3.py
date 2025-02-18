import numpy as np

def generate_cosine_signal(N, frequency):
    """Косинусный"""
    n = np.arange(N) # 0-63
    return np.cos(2 * np.pi * frequency * n / N)

def generate_constant_signal(N, value):
    """Постоянн"""
    return np.full(N, value) # 64 x 1

def generate_shifted_delta_signal(N, shift):
    """Дельта (сквад)"""
    signal = np.zeros(N) # N x 0
    signal[shift] = 1
    return signal

def compute_dft(signal):
    """ДПФ как и раньше"""
    N = len(signal)
    S = np.zeros(N, dtype=complex)
    for k in range(N):
        S[k] = np.sum(signal * np.exp(-2j * np.pi * k * np.arange(N) / N))
    return S

def compute_amplitude_phase_spectra(S):
    """Спектры"""
    amplitude_spectrum = np.abs(S)
    phase_spectrum = np.angle(S)
    return amplitude_spectrum, phase_spectrum

def print_signal_and_spectra(title, signal, amplitude_spectrum, phase_spectrum):
    """Выводы"""
    print(f"\n{title}:")
    print("Сигнал (s(n)):")
    print(np.round(signal, 3))
    print("\nАмплитудный спектр (|S(k)|):")
    print(np.round(amplitude_spectrum, 3))
    print("\nФазовый спектр (ϕ(k)):")
    print(np.round(phase_spectrum, 3))

N = 64
frequency = 5  #  для косинусного сигнала
constant_value = 1  # для постоянного сигнала
delta_shift = 16  # для дельта-импульса

cosine_signal = generate_cosine_signal(N, frequency)
constant_signal = generate_constant_signal(N, constant_value)
delta_signal = generate_shifted_delta_signal(N, delta_shift)

signals = {
    "Косинусный сигнал": cosine_signal,
    "Постоянный сигнал": constant_signal,
    "Смещённый дельта-импульс": delta_signal
}

for title, signal in signals.items():
    S = compute_dft(signal)
    amplitude_spectrum, phase_spectrum = compute_amplitude_phase_spectra(S)
    print_signal_and_spectra(title, signal, amplitude_spectrum, phase_spectrum)