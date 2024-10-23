import requests
from bs4 import BeautifulSoup
import pandas
import time
import csv
headers = {
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
}
url = 'https://www.labirint.ru/books/'

page = requests.get(url, headers = headers)
data = [['Автор-Название','Жанр', 'Цена', 'Ссылка']]
soap = BeautifulSoup(page.content, 'html.parser')
for i in soap.find_all('div', class_='pagination-number'):
    for elem in soap.find_all('div',class_="genres-carousel__item" ):
        title = "\"" + elem.find('a').get('title').strip()+"\""
        price = elem.find('div').get('data-discount-price').strip()
        author = elem.find('div').get('data-maingenre-name').strip()
        url = 'https://www.labirint.ru' + elem.find('a', class_='product-title-link').get('href').strip()
        list = [title, author, price, url]
        data.append(list)

frame = pandas.DataFrame(data)
frame.to_excel('teams.xlsx')
print('success!')










# Парсер магазина одежды
# data = [['title', 'price','color', 'url', 'photo']]
# url = "https://kith.com/collections/mens-footwear"
# def get_soup(url):
#     res = requests.get(url, headers)
#     fff = BeautifulSoup(res.content, "html.parser")
#     return fff
#
#
# for items in get_soup(url).find_all('li', class_= 'collection-product'):
#     title = items.find('h1', class_= 'product-card__title').text.strip()
#     price = items.find('span', class_= 'product-card__price').text.strip()
#     color = items.find('h2', class_='product-card__color').text.strip()
#     url = items.find("a").get('href')
#     photo = items.find('img').get('src')
#     list = [title, price, color, url, photo]
#     data.append(list)
#
# pand= pandas.DataFrame(data)
# pand.to_excel('pars.xlsx')
# print("Данные перенесены в таблицу!")


