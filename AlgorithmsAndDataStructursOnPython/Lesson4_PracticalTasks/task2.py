# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена
import cProfile


# решение без решета эратосфена

def prime_number_search(prime_number_pos):
    dividers = [2]
    prime_numbers = [2]
    candidate = prime_numbers[0]
    k = 1
    while k < prime_number_pos:
        candidate += 1
        dividers += [candidate]
        # проверяем делимость кандидата
        for divider in dividers[:-1]:
            if candidate % divider == 0:
                break
        else:
            prime_numbers += [candidate]
            k += 1
    return prime_numbers[prime_number_pos - 1]


# решение с решетом эратосфена


def prime_number_search_eratosthenes(prime_number_pos):
    prime_numbers_count = 1
    numbers = [0, 0, 2]
    while prime_numbers_count < prime_number_pos+1:
        bottom = numbers[-1]+1
        top = bottom+prime_number_pos
        numbers += list(range(bottom, top))
        m = 2
        while m < top:
            if numbers[m] != 0:
                j = m * 2
                while j < top:
                    numbers[j] = 0
                    j += m
            m += 1
        while numbers[-1] == 0:
            del numbers[-1]
        prime_numbers_count = len(set(numbers))
    numbers = [number for number in numbers if number != 0]
    return numbers[prime_number_pos-1]


cProfile.run('print(prime_number_search_eratosthenes(1000))')
cProfile.run('print(prime_number_search(1000))')
# 500ое простое число равно 3571 согласно википедии

# на моей машине prime_number_search_eratosthenes(1000) занимает 0.011
# на моей машине prime_number_search(1000) занимает 0.242
# Вывод: алгоритм эратосфена эффективней


