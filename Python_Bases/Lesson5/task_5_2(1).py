# 1.	Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:


def odd_nums_list_gen(n):
    for i in range(n):
        if i % 2 != 0:
            yield i


odd_nums = odd_nums_list_gen(int(input("Введите максимальное число для генератора нечетных чисел: ")))
print(*odd_nums)

# 2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def odd_nums_list_advanced(n):
    return (i for i in range(n) if i % 2 != 0)


odd_nums_advanced = odd_nums_list_advanced(int(input("Введите максимальное число для генератора нечетных чисел: ")))
print(*odd_nums_advanced)
