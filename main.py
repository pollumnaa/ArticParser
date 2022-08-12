# библиотека requests для создания запросов к HTML разметке веб-ресурса
# библиотека BeautifulSoup для анализа HTML кода
# библиотека csv для записи данных в csv-файл
import requests
from bs4 import BeautifulSoup
import csv

# список URL адресов сайтов со статьями
url = [
    'https://habr.com/ru/hub/machine_learning/top25/',
    'https://habr.com/ru/hub/bigdata/top25/',
    'https://habr.com/ru/hub/image_processing/top25/',
    'https://habr.com/ru/company/yandex/blog/',
    'https://habr.com/ru/company/vk/blog/',
]

# поиск нужной информации по HTML разметке сайта
for u in url:
    page = requests.get(u).text
    soup = BeautifulSoup(page, features='html.parser')
    article_list = soup.findAll(class_='tm-article-snippet__title-link')

    # получение ссылок на полученные статьи
    link_list = []
    for tag_a in soup.find_all('a'):
        if tag_a in article_list:
            link = tag_a['href']
            link_list.append('http://habr.com' + link)

    #запись данных в CSV файл
    count = 1
    with open('articles.csv', 'w', newline='') as a:
        w = csv.writer(a, delimiter=',', lineterminator='\r')
        w.writerow(['Название статьи', 'Ссылка на статью'])
        for i in range(len(article_list)):
            w.writerow([article_list[i].get_text(), link_list[i]])