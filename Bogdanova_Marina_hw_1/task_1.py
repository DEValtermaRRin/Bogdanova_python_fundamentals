# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.

time = int(input('Введите время в секундах:  '))

sec_in_min = 60
sec_in_hour = 60 * sec_in_min
sec_in_day = 24 * sec_in_hour
sec_in_month = 30 * sec_in_day  # без привязки к  конкретным месяцам (31 день и 28-29 не учитываются)
sec_in_year = 12 * sec_in_month

if 0 <= time < sec_in_min:
    print(f'{time} сек = {time} сек')
elif sec_in_min <= time < sec_in_hour:
    minute = time // sec_in_min
    sec = time % sec_in_min
    print(f'{time} сек = {minute} мин {sec} сек')
elif sec_in_hour <= time < sec_in_day:
    hour = time // sec_in_hour
    minute = (time % sec_in_hour) // sec_in_min
    sec = (time % sec_in_hour) % sec_in_min
    print(f'{time} сек = {hour} час {minute} мин {sec} сек')
elif sec_in_day <= time < sec_in_month:
    day = time // sec_in_day
    hour = (time % sec_in_day) // sec_in_hour
    minute = ((time % sec_in_day) % sec_in_hour) // sec_in_min
    sec = ((time % sec_in_day) % sec_in_hour) % sec_in_min
    print(f'{time} сек = {day} дн {hour} час {minute} мин {sec} сек')
elif sec_in_month <= time < sec_in_year:
    month = time // sec_in_month
    day = (time % sec_in_month) // sec_in_day
    hour = ((time % sec_in_month) % sec_in_day) // sec_in_hour
    minute = (((time % sec_in_month) % sec_in_day) % sec_in_hour) // sec_in_min
    sec = (((time % sec_in_month) % sec_in_day) // sec_in_hour) % sec_in_min
    print(f'{time} сек = {month} мес {day} дн {hour} час {minute} мин {sec} сек')
elif sec_in_year <= time:
    year = time // sec_in_year
    month = (time % sec_in_year) // sec_in_month
    day = ((time % sec_in_year) % sec_in_month) // sec_in_day
    hour = (((time % sec_in_year) % sec_in_month) % sec_in_day) // sec_in_hour
    minute = ((((time % sec_in_year) % sec_in_month) % sec_in_day) % sec_in_hour) // sec_in_min
    sec = ((((time % sec_in_year) % sec_in_month) % sec_in_day) % sec_in_hour) % sec_in_min
    print(f'{time} сек = {year} год {month} мес {day} дн {hour} час {minute} мин {sec} сек')
else:
    print('Вы ввели некорректное значение')
