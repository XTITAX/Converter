import string

def convert_from_base(num_str, base):
    # Конвертация числа из произвольной системы счисления в десятичную
    decimal_value = 0
    power = len(num_str) - 1
    for digit in num_str:
        if '0' <= digit <= '9':
            value = int(digit)
        else:
            value = ord(digit.lower()) - ord('a') + 10
        decimal_value += value * (base ** power)
        power -= 1
    return decimal_value

def convert_to_base(decimal_value, base):
    # Конвертация числа из десятичной системы счисления в произвольную
    if decimal_value == 0:
        return "0"
    result = ""
    while decimal_value > 0:
        remainder = decimal_value % base
        if remainder < 10:
            result = chr(remainder + ord('0')) + result
        else:
            result = chr(remainder - 10 + ord('a')) + result
        decimal_value //= base
    return result

def Convert(initial_base, final_base, number):
    # Функция для конвертации числа number из initial_base в final_base

    # Проверка на валидность входных данных
    if initial_base < 2 or final_base < 2:
        raise ValueError("Основание системы счисления должно быть не менее 2.")

    # Преобразуем число в строку, если оно не является строкой (для случаев, когда number уже строка, это не изменит его)
    num_str = str(number)

    # Конвертируем число в десятичную систему, если оно не в ней
    if initial_base != 10:
        decimal_number = convert_from_base(num_str, initial_base)
    else:
        decimal_number = int(num_str)

    # Конвертируем число из десятичной системы в final_base
    if final_base == 10:
        result = str(decimal_number)
    else:
        result = convert_to_base(decimal_number, final_base)

    return result
