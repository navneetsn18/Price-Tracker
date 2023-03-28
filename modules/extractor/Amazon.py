import requests
from bs4 import BeautifulSoup


def getAmazonData(url):
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {
        "name": soup.find('span', {'id': 'productTitle'}).text.strip(),
        "price": float(soup.find('span', {'class': 'a-price-whole'}).text.replace(',', '').replace('₹', ''))
    }
    return data
