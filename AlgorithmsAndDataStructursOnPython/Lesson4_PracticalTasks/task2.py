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
    candidate = numbers[-1]
    while prime_numbers_count < prime_number_pos:
        candidate += 1
        numbers += [candidate]
        m = 2
        while m < candidate:
            if numbers[m] != 0:
                j = m * 2
                while j <= candidate:
                    numbers[j] = 0
                    j += m
            m += 1
        if numbers[-1] != 0:
            prime_numbers_count += 1
    return numbers[-1]


cProfile.run('print(prime_number_search_eratosthenes(500))')
cProfile.run('print(prime_number_search(500))')
# 500ое простое число равно 3571 согласно википедии

# оба алгоритма возвращают правильное число но алгоритм эратосфена в данной ситуации в моей реализации проигрывает
# возможно я что-то не так реализовал но простой алгоритм работает быстрее чем алгоритм эратосфена если мы ищем
# простое число по его номеру в таблице простых чисел из за того что это решето приходится прогонять каждый раз когда
# мы переходим к следующему числу

# на моей машине prime_number_search_eratosthenes(500) занимает 1.590
# на моей машине prime_number_search(500) занимает 0.049



