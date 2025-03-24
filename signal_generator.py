import numpy as np

def generate_signal(N, signal_type, **kwargs):
    return np.random.uniform(-1, 1, N)

def print_signal_with_j(signal):
    formatted_signal = [f"{np.real(x):.3f}{np.imag(x):+.3f}j" for x in signal]
    print(formatted_signal)

def generate_cosine_signal(N, frequency):
    return np.cos(2 * np.pi * frequency * np.arange(N) / N)

def generate_constant_signal(N, value):
    return np.full(N, value)

def generate_shifted_delta_signal(N, shift):
    signal = np.zeros(N)
    signal[shift] = 1
    return signal