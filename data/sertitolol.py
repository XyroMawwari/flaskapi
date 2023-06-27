import requests
from bs4 import BeautifulSoup as bs

def serti(query):
    baseurl = 'https://tolol.ibnux.com/'
    url = baseurl+'?nama='+query
    base = bs(requests.get(url).content,
              'html.parser').find('img', class_='img-fluid rounded mt-4')['src']
    img = baseurl+base
    
    print(img)
serti('asu')
