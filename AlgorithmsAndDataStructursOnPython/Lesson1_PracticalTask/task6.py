# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
letter_number = int(input('Enter letter number in alphabet (from 1 to 26): '))
print(f'You letter is "{chr(letter_number + 96)}"')
