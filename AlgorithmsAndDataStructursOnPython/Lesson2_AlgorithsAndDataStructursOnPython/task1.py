# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые
# данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
# снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в
# качестве делителя.


while True:
    operation = input(
        'Enter math operation with two numbers and math operator divided by spaces, for example 27.5 + 32.3: ')
    operation = operation.split()
    if len(operation) != 3:
        print('Incorrect input, enter operation in requested format')
        print(f'You can perform new operation. Indicate math operator as 0 to end')
        continue
    math_operator = operation[1]
    if math_operator == '0':
        break
    number1, number2 = float(operation[0]), float(operation[2])
    if math_operator == '+':
        result = number1 + number2
    elif math_operator == '-':
        result = number1 - number2
    elif math_operator == '/':
        try:
            result = number1 / number2
        except ZeroDivisionError:
            print('Division on zero, can\'t perform operation')
            print(f'You can perform new operation. Indicate math operator as 0 to end')
            continue
    elif math_operator == '*':
        result = number1 * number2
    else:
        print('Incorrect input')
        print(f'You can perform new operation. Indicate math operator as 0 to end')
        continue
    print(f'result of operation is {result}')
    print(f'You can perform new operation. Indicate math operator as 0 to end')
print('Bye')
