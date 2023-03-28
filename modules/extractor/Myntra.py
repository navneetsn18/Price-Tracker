import requests
import json
from bs4 import BeautifulSoup


def getMyntraData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    session = requests.Session()
    res = session.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(res.text, 'html.parser')

    script = None
    for s in soup.find_all("script"):
        if 'pdpData' in s.text:
            script = s.get_text(strip=True)
            break

    jsonData = json.loads(script[script.index('{'):])

    data = {
        "name": jsonData["pdpData"]["name"],
        "price": float(jsonData["pdpData"]["sizes"][0]["sizeSellerData"][0]["discountedPrice"])
    }

    return data

