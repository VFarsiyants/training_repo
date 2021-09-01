# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letters = input('Enter two latin letters: ').lower()
first_letter = letters[0]
second_letter = letters[1]
first_position = ord(first_letter) - 96
second_position = ord(second_letter) - 96

print(f'Letter "{first_letter}" position in alphabet is "{first_position}"')
print(f'Letter "{second_letter}" position in alphabet is "{second_position}"')
print(f'Between letters "{first_letter}" and "{second_letter}" are {abs(second_position - first_position) - 1} letters')
