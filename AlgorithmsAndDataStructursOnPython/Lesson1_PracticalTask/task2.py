# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.

x1 = 5
x2 = 6

# 5 в битах 0b101 6 в битах 0b110 соответственно общий бит 0b100 операция И вернет 2^2 = 4
result = x1 & x2
print(f'Bitwise AND of numbers {x1} and {x2}')
print(f'x1 & x2 = {result}')
print(f'{bin(x1)} & {bin(x2)} = {bin(result)}\n')
# 5 в битах 0b101 6 в битах 0b110 соответственно сумма битов 0b111 операция ИЛИ вернет 2^2+2^1+2^0 = 7
result = x1 | x2
print(f'Bitwise OR of numbers {x1} and {x2}')
print(f'x1 | x2 = {result}')
print(f'{bin(x1)} | {bin(x2)} = {bin(result)}\n')
# 5 в битах 0b101, сдвиг влево на два бита 0b10100 что соответствует 2^4+2^2 = 20
result = x1 << 2
print(f'Two bits left shift for number {x1}')
print(f'{x1} << 2 = {result}')
print(f'{bin(x1)} << 2 = {bin(result)}\n')
# 5 в битах 0b101, сдвиг вправо на два бита 0b001 что соответствует 2^0 = 1
result = x1 >> 2
print(f'Two bits right shift for number {x1}')
print(f'{x1} >> 2 = {result}')
print(f'{bin(x1)} >> 2 = {bin(result)}\n')
