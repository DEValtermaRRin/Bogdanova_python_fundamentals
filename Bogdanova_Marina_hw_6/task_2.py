# 2. * Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

REZ = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ip = line.split('"')[0].split(' -')[0]
        if ip in REZ:
            REZ[ip] += 1
        else:
            REZ[ip] = 1

rez_sort = {}
keys_sorted = sorted(REZ, key=REZ.get, reverse=True)
for w in keys_sorted:
    rez_sort[w] = REZ[w]

print(REZ)
print(rez_sort)


# print(f'IP спаммера - {rez_sort.fromkeys()}, количество запросов: {rez_sort.get()}')
# медленный вариант
#
# IP_LST = []
# rez = {}
# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         ip = line.split('"')[0].split(' -')[0]
#         IP_LST.append(ip)
#
# for ip in IP_LST:
#     rez[ip] = IP_LST.count(ip)
# print(rez)
