# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

numbers = input('Enter three digits number: ')
total = 0
product = 1


for digit in numbers:
    number = int(digit)
    total += number
    product *= number

print(f'Product of number digits: {product}')
print(f'Total of number digits: {total}')
