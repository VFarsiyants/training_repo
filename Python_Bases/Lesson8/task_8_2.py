"""
*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации
вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
"Debian APT-HTTP/1.3 (0.9.7.9)"'

parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
Можно ли для них уточнить регулярное выражение?
"""

import re

PATTERN = re.compile(
    r'((?:\d{,3}\.){3}\d{,3}|(?:\w{,4}[:]){7}\w{,4}).+[\[](.+)[]]\s["](\w+)\s(\S+)\s\S+\s(\d{,4})\s(\d{,4})')
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    result = re.findall(PATTERN, data)

# for item in result:
#     print(item)
# из терминала читать не удобно, поэтому сохраняю результат в отдельный файл

with open('parse_result.txt', 'w', encoding='utf-8') as f:
    for item in result:
        f.write(str(item) + '\n')

# Особые строки, строки с IPv6 поэтому для поиска IP нужно применять условие или (|)
# Например: ('2001:4802:7801:103:8bee:6e66:ff20:475c', '31/May/2015:23:05:31 +0000', 'GET', '/downloads/product_1',
# '200', '8561')
