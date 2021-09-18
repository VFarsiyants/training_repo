# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

from itertools import zip_longest


# # не читерский способ, решаем без перевода в десятичное и обратно
hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hex_sum(number1, number2):
    """
    в основе функции лежит сложение в столбик
    :param number1: 1 слагаемое в виде списка шестнадцатиричных цифр его составляющих
    :param number2: 2ое слагаемое в виде списка шестнадцатиричных цифр его составляющих
    :return: результат суммы в виде списка шестьнадцатиричных чисел
    """
    result = []
    in_memory = 0
    for digit1, digit2 in zip_longest(number1[::-1], number2[::-1], fillvalue=0):
        digit1_dec = hex_dict[digit1] if digit1 in hex_dict.keys() else int(digit1)
        digit2_dec = hex_dict[digit2] if digit2 in hex_dict.keys() else int(digit2)
        result_digit_dec = digit1_dec + digit2_dec + in_memory
        in_memory = 0
        if result_digit_dec > 15:
            # если выходим за порядок шестьнадцатиричной цифры то 1 в "уме"
            in_memory = 1
            result_digit_dec -= 16
        if result_digit_dec > 9:
            # если больше 9 то преобразуем цифру в соответствующую букву
            hex_dict_index = list(hex_dict.values()).index(result_digit_dec)
            result_digit_hex = list(hex_dict.keys())[hex_dict_index]
        else:
            # ево всех остальных случаях десятиричная цифра соответствует 16тиричной
            result_digit_hex = str(result_digit_dec)
        result += [result_digit_hex]
    # если у нас в уме осталась единица нужно обязательно добавить порядок
    return in_memory * ['1'] + result[::-1]


def hex_product(number, factor):
    """
    В основе функции лежит умножение в столбик. Множимое число умножаем поочеродно на каждую цифру
    множителя добавля 0 справа для каждой последующей операции умножения. Само умножение представляем как
    сумму самого себя столько раз сколько требует множитель
    :param number: множимое в виде списка цифр 16тиричного числа
    :param factor: множитель в виде списка цифр 16тиричного числа
    :return: произведение в виде списка цифр 16тиричного числа
    """
    # список содержащий результаты поэтапного умножения множимого на цифры множителя "в столбик"
    intermediate_results = []
    for digit, i in zip(factor[::-1], range(len(factor))):
        current_factor = hex_dict[digit] if digit in hex_dict.keys() else int(digit)
        if current_factor == 0:
            result = (['0'] + i * ['0'])
            # при умножении на 0 получаем 0 но не забываем про сдвиг
        elif current_factor == 1:
            # при умножении на единицу получаем само число
            result = (number + i * ['0'])
        else:
            result = number
            for _ in range(current_factor - 1):
                result = hex_sum(result, number)
            result += i * ['0']
            # суммируем число само на себя согласно текущему множителю
        intermediate_results += [result]
    # суммируем результаты сложения
    if len(intermediate_results) == 1:
        return intermediate_results[0]
    else:
        result = intermediate_results[0]
        for i in range(1, len(intermediate_results)):
            result = hex_sum(result, intermediate_results[i])
        return result


hex_number1 = [digit for digit in input('Enter first hexagonal number: ')]
hex_number2 = [digit for digit in input('Enter second hexagonal number: ')]

print('Summary of hexagonal numbers')
print(hex_sum(hex_number1, hex_number2))
print('---------------------------')
print('Product of hexagonal numbers')
print(hex_product(hex_number1, hex_number2))

# читерский способ
# hex_number1 = int(input('Enter first hexagonal number: '), 16)
# hex_number2 = int(input('Enter second hexagonal number: '), 16)
#
# number_product = hex(hex_number2 * hex_number1)
# number_sum = hex(hex_number2 + hex_number1)
#
# print(f'sum of numbers is {number_sum}')
# print(f'product of numbers is {number_product}')
