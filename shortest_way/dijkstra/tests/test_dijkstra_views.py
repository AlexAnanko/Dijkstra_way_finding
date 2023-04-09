import pytest
from django.test import TestCase, Client
from ..models import News
from django.urls import reverse

class TestNewsView(TestCase):

    def test_news_view(self):
        news = News()
        news.id = 1
        news.title = "Some title"
        news.text = "Some text"
        news.link = "http//somelink1.com"
        news.save()

        test_list = News.objects.get(pk=news.id)
        self.assertEqual(test_list, news)

class TestNewsListView(TestCase):

    def test_news_list_view(self):

        response = self.client.get(reverse('news_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news_list.html')
        self.assertTemplateUsed(response, 'base12md.html')
        self.news1 = News.objects.create(
            title = "title1",
            text = "some text1",
            link = "http//somelink1.com"
        )

class TestRouteView(TestCase):

    def test_route_view(self):

        response = self.client.get(reverse('route'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'error.html')
        self.assertTemplateUsed(response, 'base12md.html')

