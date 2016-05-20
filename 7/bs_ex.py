# -*- coding: utf-8 -*-
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests
r = requests.get('http://yandex.ru')
print r.status_code
html = r.text
parsed_html = BeautifulSoup(html)
print parsed_html.title
# <title>Яндекс</title>
print parsed_html.title.string
# Яндекс

print parsed_html.body.find_all('a')

'''
 [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
'''

for link in parsed_html.body.find_all('a'):
    print link.get('href')

'''

https://tv.yandex.ua/187/channels/1532
https://tv.yandex.ua/187/program/2021782?eventId=83552254
https://tv.yandex.ua/187/channels/1468
https://tv.yandex.ua/187/program/2140477?eventId=83626898
https://tv.yandex.ua/187/channels/1489

'''


for link in parsed_html.body.find_all('a', class_='link'):
    print link.text

    '''
        Браузер попередить про заражений файл
        Карти
        Маркет
        Новини
        Перекладач
        Зображення
    '''


for li in parsed_html.body.find_all('ol', class_='list b-news-list'):
    print li.text

'''
У Путіна прокоментували розмову з Порошенком про СавченкоЄ.Єрофєєв відмовився оскаржувати рішення суду – адвокатЗахарченко розповів, коли закінчиться війна на ДонбасіКонституційний суд Росії відмовився виконувати рішення СтрасбургаІДІЛ готує теракти на європейських курортах - ЗМІ
'''



