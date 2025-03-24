from signal_generator import (
    generate_signal,
    generate_cosine_signal,
    generate_constant_signal,
    generate_shifted_delta_signal,
    print_signal_with_j,
)
from dft_operations import (
    compute_dft,
    compute_idft,
    compute_amplitude_phase_spectra,
    remove_dc_component,
    zero_first_10_harmonics,
    shift_amplitude_spectrum,
)
from file_operations import save_signal_to_file, load_signal_from_file, save_dft_to_file, load_dft_from_file

import numpy as np

ORIGINAL_SIGNAL_FILE = "original_signal.txt"
DFT_FILE = "original_signal_dft.txt"
IDFT_FILE = "original_signal_idft.txt"

COSINE_SIGNAL_FILE = "cosine_signal.txt"
CONSTANT_SIGNAL_FILE = "constant_signal.txt"
DELTA_SIGNAL_FILE = "delta_signal.txt"

def show_menu():
    print("\n--- Меню ---")
    print("1. Сгенерировать случайный сигнал и сохранить в файл")
    print("2. Вывести текущий сигнал из файла")
    print("3. Провести ДПФ над сигналом и записать в файл")
    print("4. Провести ОДПФ над сигналом из файла ДПФ")
    print("5. Рассчитать амплитудный и фазовый спектры для ДПФ сигнала из файла")
    print("6. Генерация и вывод 3-х других сигналов")
    print("7. Вычислить амплитудный и фазовый спектры для 3-х сигналов")
    print("8. Выполнить операции над сигналами")
    print("9. Выход")
    
    choice = input("Выберите пункт: ")
    
    if choice == "1":
        generate_and_save_signal()
    elif choice == "2":
        display_current_signal()
    elif choice == "3":
        perform_dft_on_signal()
    elif choice == "4":
        perform_idft_on_dft()
    elif choice == "5":
        calculate_spectra_for_dft()
    elif choice == "6":
        generate_and_save_other_signals()
    elif choice == "7":
        calculate_spectra_for_other_signals()
    elif choice == "8":
        perform_operations_on_signals()
    elif choice == "9":
        exit()
    else:
        print("Неверный выбор. Попробуйте снова.")

def generate_and_save_signal():
    N = int(input("Введите длину сигнала (N): "))
    signal = generate_signal(N, "random")
    save_signal_to_file(signal, ORIGINAL_SIGNAL_FILE)

def display_current_signal():
    signal = load_signal_from_file(ORIGINAL_SIGNAL_FILE)
    print("Текущий сигнал:")
    print_signal_with_j(signal)

def perform_dft_on_signal():
    signal = load_signal_from_file(ORIGINAL_SIGNAL_FILE)
    dft_result = compute_dft(signal)
    save_dft_to_file(dft_result, DFT_FILE)

def perform_idft_on_dft():
    dft_result = load_dft_from_file(DFT_FILE)
    idft_result = compute_idft(dft_result)
    save_signal_to_file(idft_result, IDFT_FILE)

def calculate_spectra_for_dft():
    dft_result = load_dft_from_file(DFT_FILE)
    amplitude_spectrum, phase_spectrum = compute_amplitude_phase_spectra(dft_result)
    print("Амплитудный спектр:")
    print(amplitude_spectrum)
    print("Фазовый спектр:")
    print(phase_spectrum)

def generate_and_save_other_signals():
    N = 64
    frequency = 5
    constant_value = 1
    delta_shift = 16

    cosine_signal = generate_cosine_signal(N, frequency)
    constant_signal = generate_constant_signal(N, constant_value)
    delta_signal = generate_shifted_delta_signal(N, delta_shift)

    save_signal_to_file(cosine_signal, COSINE_SIGNAL_FILE)
    save_signal_to_file(constant_signal, CONSTANT_SIGNAL_FILE)
    save_signal_to_file(delta_signal, DELTA_SIGNAL_FILE)

    print(f"Сигналы сохранены в файлы: {COSINE_SIGNAL_FILE}, {CONSTANT_SIGNAL_FILE}, {DELTA_SIGNAL_FILE}")

def calculate_spectra_for_other_signals():
    signals = {
        "Косинусный сигнал": load_signal_from_file(COSINE_SIGNAL_FILE),
        "Постоянный сигнал": load_signal_from_file(CONSTANT_SIGNAL_FILE),
        "Смещённый дельта-импульс": load_signal_from_file(DELTA_SIGNAL_FILE),
    }

    for title, signal in signals.items():
        S = compute_dft(signal)
        amplitude_spectrum, phase_spectrum = compute_amplitude_phase_spectra(S)
        print(f"\n{title}:")
        print("Амплитудный спектр:")
        print(np.round(amplitude_spectrum, 3))
        print("Фазовый спектр:")
        print(np.round(phase_spectrum, 3))

def perform_operations_on_signals():
    print("\n--- Выбор сигнала для операций ---")
    print("1. Постоянная составляющая (обнулить постоянную составляющую)")
    print("2. Косинусный сигнал")
    print("3. Смещённый дельта-импульс")
    
    signal_choice = input("Выберите сигнал: ")
    
    if signal_choice == "1":
        signal = load_signal_from_file(CONSTANT_SIGNAL_FILE)
        #S = compute_dft(signal)
        S_no_dc = remove_dc_component(signal)
        #signal_no_dc = compute_idft(S_no_dc)
        save_signal_to_file(S_no_dc, "constant_signal_no_dc.txt")
        print("Постоянная составляющая обнулена. Результат сохранён в файл constant_signal_no_dc.txt.")
    
    elif signal_choice in ["2", "3"]:
        signal_name = "cosine_signal" if signal_choice == "2" else "delta_signal"
        signal_file = COSINE_SIGNAL_FILE if signal_choice == "2" else DELTA_SIGNAL_FILE
        
        signal = load_signal_from_file(signal_file)
        S = compute_dft(signal)
        amplitude_spectrum, phase_spectrum = compute_amplitude_phase_spectra(S)
        
        print("\n--- Выбор операции ---")
        print("1. Обнулить амплитуды первых 10 гармоник")
        print("2. Выполнить циклический сдвиг амплитудного спектра на 9 отсчетов")
        
        operation_choice = input("Выберите операцию: ")
        
        if operation_choice == "1":
            modified_amplitude = amplitude_spectrum.copy()
            modified_amplitude[:10] = 0
            
            print("Исходный амплитудный спектр:")
            print(np.round(amplitude_spectrum, 3))
            print("Изменённый амплитудный спектр:")
            print(np.round(modified_amplitude, 3))

            #modified_S = modified_amplitude * np.exp(1j * phase_spectrum)
            #signal_modified = compute_idft(modified_S)
            #output_file = f"{signal_name}_zero_harmonics.txt"
            #save_signal_to_file(signal_modified, output_file)
            #print(f"Амплитуды первых 10 гармоник обнулены. Результат сохранён в файл {output_file}.")
        
        elif operation_choice == "2":
            shifted_amplitude = np.roll(amplitude_spectrum, 9)
            
            print("Исходный амплитудный спектр:")
            print(np.round(amplitude_spectrum, 3))
            print("Изменённый амплитудный спектр:")
            print(np.round(modified_amplitude, 3))

            #modified_S = shifted_amplitude * np.exp(1j * phase_spectrum)
            #signal_modified = compute_idft(modified_S)
            #output_file = f"{signal_name}_shifted_amplitude.txt"
            #save_signal_to_file(signal_modified, output_file)
            #print(f"Циклический сдвиг амплитудного спектра выполнен. Результат сохранён в файл {output_file}.")
        
        else:
            print("Неверный выбор операции.")
    
    else:
        print("Неверный выбор сигнала.")