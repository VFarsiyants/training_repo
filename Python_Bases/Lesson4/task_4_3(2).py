from requests import get, utils
from datetime import datetime
from decimal import Decimal


def get_currency(valute_name):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    # Ответ от сервера получаем в виде строки
    content = response.content.decode(encoding=encodings)
    # По строке дата всегда в одном и том же месте, срезаем ее и преобразуем в неободимый формат
    date = datetime.strptime(content[60:70], "%d.%m.%Y").date()
    # Приводим к верхнему регистру
    valute_name = valute_name.upper()
    if valute_name in content:
        # Определяю место в строке искомой валюты и режем
        content = content[content.index(valute_name):]
        # В нашем срезе нам нужно определить первое вхождение с тегом "<Value>" для отбора значения курса
        # используем Decimal для арифметического округления до копеек
        result = Decimal(content[content.index("<Value>") + 7: content.index("</Value>")].replace(",", "."))
        return result.quantize(Decimal("1.00")), date
    else:
        return None


print(f"на дату {get_currency('usd')[1]} курс доллара: {get_currency('usd')[0]}")
print(f"на дату {get_currency('eur')[1]} курс евро: {get_currency('eur')[0]}")
