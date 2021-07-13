# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    info_lst = []
    for line in f:
        row = line.split('"')
        ip = row[0].split(' -')[0]
        request_type = row[1].split('/')[0]
        requested_resource = row[1].split(' ')[1]
        info = (ip, request_type, requested_resource)
        info_lst.append(info)
    print(info_lst)