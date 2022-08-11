# библиотека requests для создания запросов к HTML разметке веб-ресурса
# библиотека BeautifulSoup для анализа HTML кода
import requests
from bs4 import BeautifulSoup
import csv

# список URL адресов сайтов со статьями
url = [
    'https://habr.com/ru/hub/machine_learning/top100/',
    'https://habr.com/ru/hub/bigdata/',
    'https://medium.com/tag/machine-learning',
    'https://towardsdatascience.com/'
]

# поиск нужной информации по HTML разметке сайта
for u in url:
    page = requests.get(u).text
    soup = BeautifulSoup(page, features="html.parser")
    title_list = soup.find_all('h2')

    # запись данных в CSV файл
    count = 1
    with open('articles.csv', 'w', newline='') as a:
        w = csv.writer(a, delimiter=',', lineterminator='\r')
        w.writerow(['Номер статьи', 'Название статьи'])
        for h in title_list:
            w.writerow(['№ ' + str(count), h.get_text()])
            count += 1