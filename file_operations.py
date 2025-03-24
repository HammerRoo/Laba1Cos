import numpy as np

def save_signal_to_file(signal, filename):
    with open(filename, "w") as f:
        for x in signal:
            f.write(f"{np.real(x):.6f}{np.imag(x):+.6f}j\n")

def load_signal_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    signal = [complex(line.strip()) for line in lines]
    return np.array(signal)

def save_dft_to_file(dft_result, filename):
    with open(filename, "w") as f:
        for x in dft_result:
            f.write(f"{np.real(x):.6f}{np.imag(x):+.6f}j\n")

def load_dft_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    dft_result = [complex(line.strip()) for line in lines]
    return np.array(dft_result)