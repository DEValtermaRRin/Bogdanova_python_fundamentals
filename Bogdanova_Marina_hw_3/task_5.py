# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
import random


def get_jokes(n, noun, adverb, adjective, verb, repeat_words):
    jokes = []
    if repeat_words:
        random.shuffle(noun)
        random.shuffle(adverb)
        random.shuffle(adjective)
        random.shuffle(verb)
        for i in range(n):
            joke = f'{adverb[i]} {adjective[i]} {noun[i]} {verb[i]}'
            jokes.append(joke)
        return jokes
    else:
        for i in range(n):
            joke = f'{random.choice(adverb)} {random.choice(adjective)} {random.choice(noun)} {random.choice(verb)}'
            jokes.append(joke)
        return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом", "кот", "крокодил"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "на рассвете"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "пушистый", "теплый"]
verbs = ['шагает', 'пляшет ', 'смотрит', 'прыгает', 'плывет', 'пишет', 'машет']


count = int(input('Сколько шуток вывести? (до 6 шуток) '))
_ = (input('Повторять слова в шутках? Да / Нет:  ')).lower()
refuse = ['нет', 'no']
repeat_word = True if _ in refuse else False


print(get_jokes(count, noun=nouns, adverb=adverbs, adjective=adjectives, verb=verbs, repeat_words=repeat_word))
