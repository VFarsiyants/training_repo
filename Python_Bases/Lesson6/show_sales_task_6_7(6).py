from sys import argv

try:
    start = int(argv[1])
except IndexError:
    pass
try:
    end = int(argv[2])
except IndexError:
    pass

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if 'start' in globals() and 'end' in globals():
        i = 0
        for line in f:
            if (i >= (start - 1)) & (i <= (end - 1)):
                print(line.strip())
            else:
                pass
            i += 1
    elif 'start' in globals():
        i = 0
        for line in f:
            if i >= (start - 1):
                print(line.strip())
            else:
                pass
            i += 1
    else:
        for line in f:
            print(line.strip())

# Комманды для проверки работы скрипта
# python "show_sales_task_6_7(6).py" 2
# python "show_sales_task_6_7(6).py" 2 4
# python "show_sales_task_6_7(6).py" 3
# python "show_sales_task_6_7(6).py"
