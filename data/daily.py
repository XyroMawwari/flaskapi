from bs4 import BeautifulSoup as bs
import requests, cloudscraper,json

def dailyquest():
    baseurl = 'https://growstocks.xyz/'
    url = bs(requests.get(baseurl).content,
             'html.parser')
    jadus = url.find('div', class_='titleBar2').text.strip()
    baseid = url.find('div', id='dqCont')
    dqone = baseid.findAll('div', class_='dqRes')
    dqones = []
    for i in dqone:
        dqoneq = i.find('a', class_='itemLink')
        judul = dqoneq.text
        link = baseurl+dqoneq['href']
        rate = i.findAll('b')[1].text
        dqones.append({'title':judul, 'link':link, 'rate':rate})

    return {
        'data':dqones,
        'price':jadus,
    }

dailyquest()
