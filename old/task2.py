import numpy as np

def compute_dft(N, s):
    # ДПФ как и в 1-м задании
    S = np.zeros(N, dtype=complex)
    for k in range(N):
        S[k] = 0
        for n in range(N):
            exponent = -2j * np.pi * k * n / N
            S[k] += s[n] * np.exp(exponent)
    return S

def compute_amplitude_phase_spectra(S):
    amplitude_spectrum = np.abs(S)
    
    phase_spectrum = np.angle(S)
    
    return amplitude_spectrum, phase_spectrum

N = int(input("Введите N: "))
s = list(map(float, input("Введите массив s(n) через пробел: ").split()))

if len(s) != N:
    print("Ошибка: длина массива s(n) должна быть равна N.")
else:
    S = compute_dft(N, s)
    
    amplitude_spectrum, phase_spectrum = compute_amplitude_phase_spectra(S)
    
    print("\nРезультаты ДПФ:")
    for k in range(N):
        print(f"S({k}) = {S[k]:.3f}")
    
    print("\nАмплитудный спектр:")
    for k in range(N):
        print(f"|S({k})| = {amplitude_spectrum[k]:.3f}")
    
    print("\nФазовый спектр:")
    for k in range(N):
        print(f"ϕ({k}) = {phase_spectrum[k]:.3f}")