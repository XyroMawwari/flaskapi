from bs4 import BeautifulSoup as bs
import requests, cloudscraper,json

def gtfandom(yatim):
    home = bs(requests.get('https://growtopia.fandom.com/wiki/Special:Search?query='+yatim).content,
              'html.parser').find('a', class_='unified-search__result__title')['href']
    base = bs(requests.get(home).content,
              'html.parser')
    img = base.find('span', class_='mw-headline').find('img')['src']
    title = base.find('span', class_='mw-page-title-main').text 
    desk = base.find('div', class_='card-text').text
    table = base.find('table', class_='card-field')
    tr = table.findAll('tr')
    data_ = []
    for i in tr:
        desj = i.find('th').text
        data = i.find('td').text
        #print(data)
        data_.append({'title':desj, 'data':data})
    return {
        'image':img,
        'title':title,
        'description':desk,
        'data':data_,
                }