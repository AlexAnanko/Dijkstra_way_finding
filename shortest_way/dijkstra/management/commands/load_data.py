from itertools import count
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
import json
from dijkstra.models import News

def news():
    """
    This function get the request to the link and take from that titles, text and links of article on the site.
    Then it creates news.json file which is recorded into model News.

    :return: news.json file
    """

    articles_found = []
    art_text = []
    links_list = []
    common_list_of_news = []
    row = []

    # Get the request from www.nytimes.com/international
    res = requests.get('https://www.nytimes.com/international/')
    # Take html code of the page
    soup = BeautifulSoup(res.text, "html.parser")

    # Search tegs with articles, their text and link to the all text of article
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

    # Create a dict of title, text and link of every article
    for i in common_list_of_news:
        dict_news = {"title": i[0], "text": i[1],"link": i[2]}
        row.append(dict_news)

    # Create a json file news.json with title,text and links
    with open("dijkstra/news.json", 'w') as w_file:
        json.dump(row, w_file)

class Command(BaseCommand):
    """
    This function read json file news.json and then write it's data into News model.

    """
    def handle(self, *args, **options):

        # Open the news.json file to read
        with open('dijkstra/news.json', 'rb') as f:
            data = json.load(f)

            # Write data into News model
            for i in data:
                news = News()
                news.title = i["title"]
                news.text = i["text"]
                news.link = i["link"]
                news.save()
