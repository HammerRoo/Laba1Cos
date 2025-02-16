import numpy as np

def generate_cosine_signal(N, frequency):
    n = np.arange(N)
    return np.cos(2 * np.pi * frequency * n / N)

def generate_constant_signal(N, value):
    return np.full(N, value)

def generate_shifted_delta_signal(N, shift):
    signal = np.zeros(N)
    signal[shift] = 1
    return signal

def compute_dft(signal):
    N = len(signal)
    S = np.zeros(N, dtype=complex)
    for k in range(N):
        S[k] = np.sum(signal * np.exp(-2j * np.pi * k * np.arange(N) / N))
    return S

def compute_amplitude_phase_spectra(S):
    amplitude_spectrum = np.abs(S)
    phase_spectrum = np.angle(S)
    return amplitude_spectrum, phase_spectrum

def compute_idft(S):
    N = len(S)
    signal = np.zeros(N, dtype=complex)
    for n in range(N):
        signal[n] = np.sum(S * np.exp(2j * np.pi * n * np.arange(N) / N)) / N
    return signal

def remove_dc_component(S):
    S_new = S.copy()
    S_new[0] = 0
    return S_new

def zero_first_10_harmonics(S):
    S_new = S.copy()
    S_new[1:11] = 0
    S_new[-10:] = 0
    return S_new

def shift_amplitude_spectrum(S, shift):
    amplitude_spectrum = np.abs(S)
    phase_spectrum = np.angle(S)
    shifted_amplitude = np.roll(amplitude_spectrum, shift)
    S_new = shifted_amplitude * np.exp(1j * phase_spectrum) # Восстанавливаем комплексный спектр
    return S_new

def print_signal_and_spectra(title, signal, amplitude_spectrum, phase_spectrum):
    print(f"\n{title}:")
    print("Сигнал (s(n)):")
    print(np.round(signal, 3))
    print("\nАмплитудный спектр (|S(k)|):")
    print(np.round(amplitude_spectrum, 3))
    print("\nФазовый спектр (ϕ(k)):")
    print(np.round(phase_spectrum, 3))

N = 64
frequency = 5
constant_value = 1
delta_shift = 16

cosine_signal = generate_cosine_signal(N, frequency)
constant_signal = generate_constant_signal(N, constant_value)
delta_signal = generate_shifted_delta_signal(N, delta_shift)

signals = {
    "Косинусный сигнал": cosine_signal,
    "Постоянный сигнал": constant_signal,
    "Смещённый дельта-импульс": delta_signal
}

for title, signal in signals.items():
    print(f"\n--- Обработка сигнала: {title} ---")
    
    S = compute_dft(signal)
    amplitude_spectrum, phase_spectrum = compute_amplitude_phase_spectra(S)
    print_signal_and_spectra("Исходный спектр", signal, amplitude_spectrum, phase_spectrum)

    S_no_dc = remove_dc_component(S)
    signal_no_dc = compute_idft(S_no_dc)
    amplitude_no_dc, phase_no_dc = compute_amplitude_phase_spectra(S_no_dc)
    print_signal_and_spectra("После удаления постоянной составляющей", signal_no_dc, amplitude_no_dc, phase_no_dc)

    S_zero_harmonics = zero_first_10_harmonics(S)
    signal_zero_harmonics = compute_idft(S_zero_harmonics)
    amplitude_zero_harmonics, phase_zero_harmonics = compute_amplitude_phase_spectra(S_zero_harmonics)
    print_signal_and_spectra("После обнуления первых 10 гармоник", signal_zero_harmonics, amplitude_zero_harmonics, phase_zero_harmonics)

    S_shifted = shift_amplitude_spectrum(S, 9)
    signal_shifted = compute_idft(S_shifted)
    amplitude_shifted, phase_shifted = compute_amplitude_phase_spectra(S_shifted)
    print_signal_and_spectra("После циклического сдвига амплитудного спектра", signal_shifted, amplitude_shifted, phase_shifted)