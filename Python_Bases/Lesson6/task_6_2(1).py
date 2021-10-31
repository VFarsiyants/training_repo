# 1.	Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# 2.	*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.


from requests import get, utils

# для получения файла лога с сервера, (возможно излишне)

# response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
# encodings = utils.get_encoding_from_headers(response.headers)
# content = response.content.decode(encoding=encodings)
# with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
#     f.write(content)

# Вытягиваем из файла необходимые по условию задачи данные в виде списка кортежей
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    log_lines = []
    for line in f:
        log_line = line.split(' ')
        log_lines.append((log_line[0], log_line[5], log_line[6]))
    for line in log_lines:
        print(line)

print('______________________________________________________________________________________')

# Код для определения ip адреса спаммера
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    ip_list = []
    qtys = []
    for line in f:
        ip = line.split(' ')[0]
        if ip not in ip_list:
            ip_list.append(ip)
            qtys.append(1)
        else:
            qtys[ip_list.index(ip)] += 1
    spammer_ip = ip_list[qtys.index(max(qtys))]
    print('спаммер', spammer_ip)
