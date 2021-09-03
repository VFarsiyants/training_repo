# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
# его цифр.

numbers = input('Enter positive integer numbers divided by space: ').split()
max_digits_sum = 0
max_digits_sum_number = 0
for number in numbers:
    digit_sum = sum([int(digit) for digit in number])
    if digit_sum > max_digits_sum:
        max_digits_sum = digit_sum
        max_digits_sum_number = number
print(f'Number with the biggest sum of digits is {max_digits_sum_number}')
print(f'Sum of its\' digits is {max_digits_sum}')
