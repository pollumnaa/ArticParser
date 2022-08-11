# подключаем нужные модули
import requests
from bs4 import BeautifulSoup

# берем адрес нужной статьи и считываем текст
#url = 'https://habr.com/ru/post/681734/'
#page = requests.get(url).text

# превращаем его в объект BS, чтобы читать html-теги
#soup = BeautifulSoup(page,  features="html.parser")
#headline = soup.find('h1').get_text()
#print('НАЗВАНИЕ СТАТЬИ: ', headline)


url = [
    'https://habr.com/ru/hub/machine_learning/top100/'
    ]


for i in url:
    page = requests.get(i).text
    soup = BeautifulSoup(page,  features="html.parser")
    headline_list = soup.find_all('h2')
    for j in headline_list:
        print('=> ', j.get_text())




# весь текст статьи заключен между тегами p \p, считываем его и выводим на экран
#p_tags = soup.find_all('p')
#p_tags_text = [tag.get_text().strip() for tag in p_tags]
#article = ' '.join(p_tags_text)

#print('ТЕКСТ СТАТЬИ: ')
#for i in p_tags_text:
#    print(i)
