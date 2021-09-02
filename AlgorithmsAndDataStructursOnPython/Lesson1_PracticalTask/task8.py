# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Insert year number: '))

if year % 4 != 0:
    print(f'{year} is regular year')
elif year % 100 != 0:
    print(f'{year} is leap year')
elif year % 400 == 0:
    print(f'{year} is leap year')
else:
    print(f'{year} is regular year')
