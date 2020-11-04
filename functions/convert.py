from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount: Decimal, cur_from: str, cur_to: str, date: str = None) -> Decimal:
    if date == None:
        response = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp")
    else:
        response = requests.get(f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}")
    soup = BeautifulSoup(response.content, 'xml')
    if cur_from == 'RUR':
        valute = Decimal(str(soup.find('CharCode', text=f'{cur_to}').find_next_sibling('Value').string)
                         .replace(',', '.'))
        nominal = Decimal(str(soup.find('CharCode', text=f'{cur_to}').find_next_sibling('Nominal').string)
                          .replace(',', '.'))
        result = Decimal(amount / valute * nominal)
    elif cur_to == 'RUR':
        valute = Decimal(str(soup.find('CharCode', text=f'{cur_from}').find_next_sibling('Value').string)
                         .replace(',', '.'))
        nominal = Decimal(str(soup.find('CharCode', text=f'{cur_from}').find_next_sibling('Nominal').string)
                          .replace(',', '.'))
        result = Decimal(amount * valute * nominal)
    else:
        to_v = Decimal(str(soup.find('CharCode', text=f'{cur_to}').find_next_sibling('Value').string)
                       .replace(',', '.'))
        to_n = Decimal(str(soup.find('CharCode', text=f'{cur_to}').find_next_sibling('Nominal').string)
                       .replace(',', '.'))
        from_v = Decimal(str(soup.find('CharCode', text=f'{cur_from}').find_next_sibling('Value').string)
                         .replace(',', '.'))
        from_n = Decimal(str(soup.find('CharCode', text=f'{cur_from}').find_next_sibling('Nominal').string)
                         .replace(',', '.'))
        rub = Decimal(from_v * amount / from_n)
        result = Decimal((rub / to_v * to_n))
    return result.quantize(Decimal("1.0000"))
