from bs4 import BeautifulSoup as bs
import requests, cloudscraper,json

def price(kanjut):
    home = bs(requests.get('https://growstocks.xyz/search?item='+kanjut).content,
              'html.parser').find('a', class_='itemLink')['href']
    baseurl = 'https://growstocks.xyz/'
    url = baseurl+home
    base = bs(requests.get(url).content,
              'html.parser')
    title = base.find('h2', class_='openInformation').text
    stats = base.find('div', class_='itemChipHead')
    pricestat = base.find('div', class_='greenRow').text
    p = stats.findAll('p')
    prices = p[0].find('b').text
    rate = p[1].find('b').text
    return {
        'title':title,
        'status':pricestat,
        'result':{
            'price':prices,
            'rate':rate,
        }
    }

print(json.dumps(price('magplant'), indent=4))
