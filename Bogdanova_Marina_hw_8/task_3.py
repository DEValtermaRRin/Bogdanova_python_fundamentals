#  Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
#  можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
#  Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
def type_logger(function):
    log_list = []

    def logging_types(*args):
        result = function(args[0])
        rez = f'{args[0]}: {type(args[0])}'
        print(rez)
        if args not in log_list:
            log_list.append(rez)
        print(log_list)
        return result

    return logging_types


@type_logger
def calc_cube(x):
    return x ** 3




print(calc_cube(1))
print(calc_cube(2))
print(calc_cube(3))
print(calc_cube(4))
print(calc_cube(5))
print(calc_cube(6))
