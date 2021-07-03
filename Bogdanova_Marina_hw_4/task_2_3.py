from requests import get
import datetime


def take_content(url):
    rez = []
    resp = get(url)
    cont = resp.content.decode(encoding=resp.encoding)
    for el in cont.split('<Valute'):
        val = el.split('</')  # type list
        rez.append(val)
    return rez


def take_values(lst):
    val_dict = {}
    for val in lst[1:]:
        char_code = val[1][-3:]
        name = val[3][14:]
        value_str = val[4][12:]
        value = round(float('.'.join(value_str.split(','))), 2)
        val_dict[char_code] = [name] + [value]
    return val_dict


def take_date(lst):
    for info in lst[0]:
        date_str = info[info.find('Date=') + 6:info.find('Date=') + 16]
        date = datetime.datetime.strptime(date_str, '%d.%m.%Y')
        return date


def currency_rates(code):
    """ возможные значения: AUD AZN GBP AMD BYN BGN BRL HUF HKD DKK USD EUR INR KZT CAD
     KGS CNY MDL NOK PLN RON XDR SGD TJS TRY TMT UZS UAH CZK SEK CHF ZAR KRW JPY """

    code = code.upper()
    if code in VALUTE_DCT.keys():
        print(f'{take_date(valute_lst)}: 1 {VALUTE_DCT.get(code)[0]} ( {code} ) = {VALUTE_DCT.get(code)[1]} руб.')
    else:
        return None


valute_lst = take_content('http://www.cbr.ru/scripts/XML_daily.asp')
VALUTE_DCT = take_values(valute_lst)

user_val = input('Введите код валюты:  ')
currency_rates(user_val)
currency_rates('usd')
currency_rates('EUR')


