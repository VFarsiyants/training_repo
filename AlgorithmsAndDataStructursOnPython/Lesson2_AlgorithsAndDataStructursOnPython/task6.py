# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

qty_tries = 10
number = random.randint(0, 100)
try_counter = 0
print('Random number is set, try to guess')
while try_counter < qty_tries:
    user_number = int(input('Enter your number: '))
    if user_number < number:
        print('Your number is smaller then set number')
        try_counter += 1
    elif user_number > number:
        print('Your number is bigger then set number')
        try_counter += 1
    else:
        print(f'Yes, set number is {user_number}, you won')
        break
else:
    print('You didn\'t make it in 10 tries, you lose')
