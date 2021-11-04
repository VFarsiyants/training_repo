# 3.	Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
#
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
# чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Василий', 'Инокентий', 'Гаврила'
    # Василий, Гаврила и Инокентий добавлены для проверки когда классов меньше чеи учителей
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutor_klass = ((tutors[i], klasses[i] if i < len(klasses) else None) for i in range(len(tutors)))

print(type(tutor_klass), *tutor_klass) # доказываем что создали генератор, проходим по всем слайдам

# print(next(tutor_klass)) # для проверки генератора на истощение после итерирования по всем элементам,
# возвращает ошибку: StopIteration