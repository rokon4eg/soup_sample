from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    result =''
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    # if requests == '':
    response = requests.get(url, params = {'date_req': date})
    if response.status_code == 200:
        # print(response.content)
        soup = BeautifulSoup(response.content, 'lxml')
        currency = soup.find('charcode' , text=cur_to)
        # print(currency)
        nominal = Decimal(currency.find_next_sibling('nominal').text)
        value = Decimal(currency.find_next_sibling('value').text.replace(',','.'))
        result = Decimal(amount) * nominal / value
        if cur_from == 'RUR':
            return round(result, 4)
        else:
            currency = soup.find('charcode', text=cur_from)
            # print(currency)
            nominal = Decimal(currency.find_next_sibling('nominal').text)
            value = Decimal(currency.find_next_sibling('value').text.replace(',', '.'))
            return round(result*value/nominal,4)

    # Использовать переданный requests
    # ...
    # result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой


