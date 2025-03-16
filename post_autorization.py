import requests
from requests import Session
from bs4 import BeautifulSoup
from time import *

headers = {'User-Agent': 'CrookedHands/2.0 (EVM x8), CurlyFingers20/1;p'}

work = Session()

work.get('https://quotes.toscrape.com/', headers=headers)

response = work.get('https://quotes.toscrape.com/login', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')

data = {'csrf_token':token, 'username':'123', 'password':'1234'}

res = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)

print(res.text)