import numpy as np

def compute_dft(signal):
    N = len(signal)
    S = np.zeros(N, dtype=complex)
    for k in range(N):
        S[k] = np.sum(signal * np.exp(-2j * np.pi * k * np.arange(N) / N))
    return S

def compute_idft(S):
    N = len(S)
    signal = np.zeros(N, dtype=complex)
    for n in range(N):
        signal[n] = np.sum(S * np.exp(2j * np.pi * n * np.arange(N) / N)) / N
    return signal

# def compute_dft_trig(signal):
#     N = len(signal)
#     S = np.zeros(N, dtype=complex)
#     for k in range(N):
#         real_part = 0
#         imag_part = 0
#         for n in range(N):
#             angle = 2 * np.pi * k * n / N
#             real_part += signal[n] * np.cos(angle)
#             imag_part -= signal[n] * np.sin(angle)
#         S[k] = real_part + 1j * imag_part
#     return S

# def compute_idft_trig(S):
#     N = len(S)
#     signal = np.zeros(N, dtype=complex)
#     for n in range(N):
#         real_part = 0
#         imag_part = 0
#         for k in range(N):
#             angle = 2 * np.pi * k * n / N
#             real_part += S[k].real * np.cos(angle) - S[k].imag * np.sin(angle)
#             imag_part += S[k].real * np.sin(angle) + S[k].imag * np.cos(angle)
#         signal[n] = (real_part + 1j * imag_part) / N
#     return signal

def compute_amplitude_phase_spectra(S):
    amplitude_spectrum = np.abs(S)
    phase_spectrum = np.angle(S)
    return amplitude_spectrum, phase_spectrum

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
    S_new = shifted_amplitude * np.exp(1j * phase_spectrum)
    return S_new