from bs4 import BeautifulSoup
import requests

def exchange_rate(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find('span', class_ = 'ccOutputRslt').get_text()
    rate = float(rate[:-4])

    return rate

current_rate = exchange_rate('USD', 'PLN')
print (current_rate)