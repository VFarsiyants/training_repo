# 5.	Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
# можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
from random import choice


def get_jokes(n, can_repeat=True):
    """
    Function returns list of random jokes consist words from static lists
    :param n: quantity of jokes in returned list
    :param can_repeat: boolean, allows or prohibits to use same word in different jokes
    :return: list of random jokes consist words from static lists
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    # Если можно повторяться то просто берем образец из списка, если нет то вытягиваем его из списка с удалением
    return [f'{choice(nouns) if can_repeat else nouns.pop(nouns.index(choice(nouns)))} '
            f'{choice(adverbs) if can_repeat else adverbs.pop(adverbs.index(choice(adverbs)))} '
            f'{choice(adjectives) if can_repeat else adjectives.pop(adjectives.index(choice(adjectives)))}'
            for i in range(n)]


print(get_jokes(n=3))
print(get_jokes(can_repeat=False, n=5))
