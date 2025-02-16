import numpy as np

def compute_dft(N, s):
    """Вычисление ДПФ."""
    S = np.zeros(N, dtype=complex) # массив хранить результаты
    
    for k in range(N):
        S[k] = 0  # для суммы
        print(f"Для k = {k}")
        print(f"S({k}) = формула = подставляем = ответ")
        # тут рассчеты для вывода в консоль
        for n in range(N):
            exponent = -2j * np.pi * k * n / N # считаем по формуле
            S[k] += s[n] * np.exp(exponent) # заносим в сумму
            term = s[n] * np.exp(exponent)
            print(f"при n = {n}: {s[n]} * e^(-j * 2π * {k} * {n} / {N}) = {term:.3f}")
        print(f"S({k}) = суммируем все при n = 0..{N-1}: {S[k]:.3f}")
        print()
    
    return S

def compute_idft(N, S):
    """Вычисление ОДПФ."""
    s = np.zeros(N, dtype=complex)
    
    for n in range(N):
        s[n] = 0
        print(f"Для n = {n}")
        print(f"s({n}) = формула = подставляем = ответ")
        for k in range(N):
            exponent = 2j * np.pi * k * n / N
            s[n] += S[k] * np.exp(exponent)
            term = S[k] * np.exp(exponent) / N
            print(f"при k = {k}: {S[k]:.3f} * e^(j * 2π * {k} * {n} / {N}) / {N} = {term:.3f}")
            
        s[n] /= N

        print(f"s({n}) = суммируем все при k = 0..{N-1}: {s[n]:.3f}")
        print()
    
    return s

N = int(input("Введите N: "))
s = list(map(float, input("Введите массив s(n) через пробел: ").split()))

if len(s) != N:
    print("Ошибка: длина массива s(n) должна быть равна N.")
else:
    S = compute_dft(N, s)
    
    reconstructed_s = compute_idft(N, S)
    
    print("\nСравнение исходного и восстановленного сигналов:")
    for n in range(N):
        print(f"Исходный s({n}) = {s[n]:.3f}, Восстановленный s({n}) = {np.real(reconstructed_s[n]):.3f}")