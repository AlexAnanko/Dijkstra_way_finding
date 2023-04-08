from itertools import count
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
import json
from dijkstra.models import News

def news():

    articles_found = []
    art_text = []
    links_list = []
    common_list_of_news = []
    row = []

    res = requests.get('https://www.nytimes.com/international/')
    soup = BeautifulSoup(res.text, "html.parser")

    articles = soup.find_all('h3', class_="indicate-hover")
    articles_text = soup.find_all('p', class_="summary-class")
    links = soup.find_all('a', class_="css-9mylee")

    for article in articles:
        article = article.text
        articles_found.append(article)

    for article_text in articles_text:
        article_text = article_text.text
        art_text.append(article_text)

    for link in links:
        link = link.get('href')
        links_list.append(link)

    for i in range(0, len(art_text)):
        article = articles_found[i]
        text = art_text[i]
        link = links_list[i]

        new = article + '=>' + text + '=>' + link
        new = new.split('=>')
        common_list_of_news.append(new)


    for i in common_list_of_news:
        dict_news = {"title": i[0], "text": i[1],"link": i[2]}
        row.append(dict_news)


    with open("news.json", 'w') as w_file:
        json.dump(row, w_file)

class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('news.json', 'rb') as f:
            data = json.load(f)

            for i in data:
                news = News()
                news.title = i["title"]
                news.text = i["text"]
                news.link = i["link"]
                news.save()
        # print('finished')
