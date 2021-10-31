import sys
from utils import get_currency

print(f"на дату {get_currency(sys.argv[1])[1]} курс {sys.argv[1].upper()}: {get_currency(sys.argv[1])[0]}")

# пример команды для запуска из консоли: python task_4_5(4).py NOK
