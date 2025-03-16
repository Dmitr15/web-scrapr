import requests

from bs4 import BeautifulSoup
from time import *

list_card_url=[]
headers = {'User-Agent': 'CrookedHands/2.0 (EVM x8), CurlyFingers20/1;p'}

def download(url):
    resp = requests.get(url, stream=True)
    img=open('C:\\Users\\dovsy\\Desktop\\img_scrap\\'+url.split('/')[-1], 'wb')
    for val in resp.iter_content(1024*1024):
        img.write(val)
    img.close()

def get_url():
    for count in range(1, 7):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        data = soup.find_all('div', class_='w-full rounded border')

        for i in data:
            card_url='https://scrapingclub.com'+i.find('a').get('href')
            yield card_url

def get_arr():
    for card_url in get_url():
        resp = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(resp.text, 'lxml')
        data = soup.find('div', class_='my-8 w-full rounded border')

        name =data.find('h3').text
        price=data.find('h4').text
        descrip = data.find('p').text
        url_img='https://scrapingclub.com'+data.find('img').get('src')

        download(url_img)
        yield name, price, descrip, url_img